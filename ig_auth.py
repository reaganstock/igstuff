import asyncio
import json
import random
from playwright.async_api import async_playwright
from urllib.parse import urlencode

async def add_human_delay(page, min_delay=500, max_delay=1500):
    delay = random.randint(min_delay, max_delay)
    await asyncio.sleep(delay / 1000)

async def authenticate_account(page, username, password):
    try:
        await page.goto("https://www.instagram.com/accounts/login/", timeout=60000)
        await add_human_delay(page)
        await page.fill('input[name="username"]', username)
        await add_human_delay(page)
        await page.fill('input[name="password"]', password)
        await add_human_delay(page)
        await page.click('button[type="submit"]')
        await page.wait_for_load_state("networkidle", timeout=60000)
        
        if await page.is_visible("text=Enter the code"):
            return "Code Required"
        elif await page.is_visible('svg[aria-label="Home"]', timeout=30000):
            return "Success"
        else:
            return "Failed"
    except Exception as e:
        print(f"Error during authentication: {str(e)}")
        return "Error"

async def process_batch(batch_accounts, batch_profile_ids, api_key):
    async with async_playwright() as p:
        browsers = []
        pages = []
        for profile_id in batch_profile_ids:
            try:
                query = urlencode({
                    'x-api-key': api_key,
                    'config': json.dumps({'headless': False, 'autoClose': False}),
                })
                browser_ws_endpoint = f"ws://localhost:8848/devtool/launch/{profile_id}?{query}"
                browser = await p.chromium.connect_over_cdp(browser_ws_endpoint, timeout=60000)
                browsers.append(browser)
                pages.append(browser.contexts[0].pages[0])
            except Exception as e:
                print(f"Error connecting to profile {profile_id}: {str(e)}")

        results = {}
        successful_logins = 0
        account_index = 0

        while successful_logins < len(pages) and account_index < len(batch_accounts):
            tasks = []
            for i, page in enumerate(pages):
                if i not in results or results[i] != "Success":
                    if account_index < len(batch_accounts):
                        username, password, _, _, _ = batch_accounts[account_index]
                        tasks.append(authenticate_account(page, username, password))
                        account_index += 1
                    else:
                        break

            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, result in enumerate(batch_results):
                if isinstance(result, Exception):
                    print(f"Error on profile {batch_profile_ids[i]}: {str(result)}")
                    results[i] = "Error"
                elif i not in results or results[i] != "Success":
                    results[i] = result
                    if result == "Success":
                        successful_logins += 1
                        print(f"Successfully logged in on profile {batch_profile_ids[i]}")
                    else:
                        print(f"Login attempt on profile {batch_profile_ids[i]} resulted in: {result}")

            if successful_logins >= len(pages):
                break

        for browser in browsers:
            try:
                await browser.close()
            except:
                pass

        return results

async def main():
    api_key = input("Enter your NST Browser API key: ")
    
    with open('clients/graham/accounts.txt', 'r') as f:
        accounts = [line.strip().split(':') for line in f]
    
    with open('profile_ids.txt', 'r') as f:
        profile_ids = [line.strip() for line in f]
    
    all_results = {}
    
    for i in range(0, len(profile_ids), 10):
        batch_profile_ids = profile_ids[i:i+10]
        batch_accounts = accounts[i:]  # Use all remaining accounts
        
        print(f"\nProcessing batch {i//10 + 1}")
        batch_results = await process_batch(batch_accounts, batch_profile_ids, api_key)
        
        print(f"Batch {i//10 + 1} completed. Results:")
        for profile_id, result in zip(batch_profile_ids, batch_results.values()):
            print(f"Profile {profile_id}: {result}")
        
        all_results.update({f"Profile {pid}": result for pid, result in zip(batch_profile_ids, batch_results.values())})
        
        successful_logins = sum(1 for result in batch_results.values() if result == "Success")
        print(f"Successful logins in this batch: {successful_logins}/{len(batch_results)}")
        
        if successful_logins < len(batch_results):
            print("Not all profiles were logged in. Stopping the process.")
            break
    
    print("\nOverall Login Attempt Summary:")
    for profile, result in all_results.items():
        print(f"{profile}: {result}")
    
    total_successful = sum(1 for result in all_results.values() if result == "Success")
    print(f"\nTotal successful logins: {total_successful}/{len(all_results)}")

asyncio.run(main())
