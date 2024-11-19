import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from urllib.parse import urlencode
import json
import random
import datetime
from typing import Dict, List
from dataclasses import dataclass

API_KEY = "9eb7357f-ed4b-45e7-beac-d0b1db34c2e4"

@dataclass
class InstagramAccount:
    username: str
    password: str
    email: str
    email_password: str
    creation_year: str

    @classmethod
    def from_line(cls, line: str) -> 'InstagramAccount':
        try:
            parts = line.strip().split(':')
            
            # Handle different format cases
            if len(parts) == 4:  # Missing year
                parts.append("2016")
            elif len(parts) == 3:  # Username:email:password format
                username, email, password = parts
                return cls(username=username, 
                         password=password,
                         email=email,
                         email_password=password,  # Using same password for email
                         creation_year="2016")
                
            if len(parts) != 5:
                raise ValueError(f"Invalid line format: {line}")
                
            username, password, email, email_pass, year = parts
            return cls(username, password, email, email_pass, year)
        except Exception as e:
            print(f"Warning: Invalid line format: {line}")
            raise

async def handle_login_attempt(context, account: InstagramAccount):
    try:
        # Create Instagram login tab
        instagram_page = await context.new_page()
        await instagram_page.goto("https://www.instagram.com/accounts/login/", timeout=90000)
        await instagram_page.fill('input[name="username"]', account.username)
        await instagram_page.fill('input[name="password"]', account.password)
        await instagram_page.click('button[type="submit"]')
        
        # Create Outlook login tab
        outlook_page = await context.new_page()
        await outlook_page.goto("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=165&ct=1731535907&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1")
        
        # Fill Outlook credentials
        await outlook_page.get_by_test_id("i0116").fill(account.email)
        await outlook_page.get_by_test_id("i0116").press("Enter")
        await outlook_page.wait_for_timeout(2000)
        await outlook_page.get_by_test_id("i0118").fill(account.email_password)
        await outlook_page.get_by_test_id("i0118").press("Enter")
        await outlook_page.wait_for_load_state('networkidle')
        await outlook_page.
        
        
        return "Login attempts initiated"

    except Exception as e:
        print(f"Error during login process for {account.username}: {str(e)}")
        return f"Error: {str(e)}"

async def process_batch(playwright, accounts: List[InstagramAccount], profile_ids: List[str], api_key: str):
    active_browsers = []
    results = {}
    
    try:
        # Launch browsers for the batch
        for account, profile_id in zip(accounts, profile_ids):
            try:
                query = urlencode({
                    'x-api-key': api_key,
                    'config': json.dumps({'headless': False, 'autoClose': False}),
                })
                browser_ws_endpoint = f"ws://localhost:8848/devtool/launch/{profile_id}?{query}"
                
                print(f"\nLaunching profile for {account.username}")
                browser = await playwright.chromium.connect_over_cdp(browser_ws_endpoint)
                context = browser.contexts[0]
                
                result = await handle_login_attempt(context, account)
                results[account.username] = result
                active_browsers.append((browser, account.username))
                
            except Exception as e:
                print(f"Failed to process {account.username}: {str(e)}")
                results[account.username] = f"Error: {str(e)}"
    
        # Print batch results
        print("\nBatch Results:")
        for username, result in results.items():
            print(f"{username}: {result}")
        
        # Wait for user confirmation
        while True:
            response = input("\nHave you completed verification for all accounts? (Y/N): ").strip().upper()
            if response == 'Y':
                break
            elif response == 'N':
                print("Please complete verification before continuing...")
            else:
                print("Please enter Y or N")
    
    finally:
        # Clean up browsers
        print("\nClosing browsers...")
        for browser, username in active_browsers:
            try:
                await browser.close()
                print(f"Closed browser for {username}")
            except Exception as e:
                print(f"Error closing browser for {username}: {str(e)}")
    
    return results

async def main():
    api_key = API_KEY
    
    try:
        # Load all accounts
        with open('accounts.txt', 'r') as f:
            all_accounts = []
            for line_num, line in enumerate(f, 1):
                try:
                    if line.strip():  # Skip empty lines
                        account = InstagramAccount.from_line(line)
                        all_accounts.append(account)
                except Exception as e:
                    print(f"Skipping invalid account at line {line_num}")
                    continue
        
        if not all_accounts:
            print("No valid accounts found in accounts.txt")
            return
        
        # Load all profile IDs
        try:
            with open('profile_ids.txt', 'r') as f:
                all_profile_ids = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("profile_ids.txt not found!")
            return
        
        if len(all_profile_ids) < len(all_accounts):
            print(f"\nWarning: Not enough profile IDs ({len(all_profile_ids)}) for all accounts ({len(all_accounts)})")
            all_accounts = all_accounts[:len(all_profile_ids)]
        
        # Process in batches of 10
        batch_size = 10
        all_results = {}
        
        async with async_playwright() as playwright:
            for i in range(0, len(all_accounts), batch_size):
                batch_accounts = all_accounts[i:i + batch_size]
                batch_profile_ids = all_profile_ids[i:i + batch_size]
                
                print(f"\nProcessing batch {(i//batch_size) + 1} of {(len(all_accounts) + batch_size - 1)//batch_size}")
                print(f"Accounts in this batch: {[acc.username for acc in batch_accounts]}")
                
                batch_results = await process_batch(playwright, batch_accounts, batch_profile_ids, api_key)
                all_results.update(batch_results)
                
                if i + batch_size < len(all_accounts):
                    print("\nBatch complete. Starting next batch in 5 seconds...")
                    await asyncio.sleep(5)
        
        # Print final results
        print("\nFinal Results:")
        for username, result in all_results.items():
            print(f"{username}: {result}")
            
    except FileNotFoundError:
        print("accounts.txt not found!")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())