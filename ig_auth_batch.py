import asyncio
import json
import random
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from urllib.parse import urlencode
import os
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import aiohttp
from datetime import datetime

@dataclass
class InstagramAccount:
    username: str
    password: str
    email: str
    email_password: str
    creation_year: str

    @classmethod
    def from_line(cls, line: str) -> Optional['InstagramAccount']:
        try:
            parts = line.strip().split(':')
            if len(parts) != 5:
                print(f"Warning: Skipping malformed line (expected 5 parts, got {len(parts)}): {line}")
                return None
            username, password, email, email_pass, year = parts
            return cls(username, password, email, email_pass, year)
        except Exception as e:
            print(f"Error parsing line: {line}")
            print(f"Error details: {str(e)}")
            return None

class SMSPVAClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.smspva.com"
        self.country = "ES"  # Spain
        self.service = "opt15"  # Microsoft service code
        self.current_order_id = None

    async def _make_request(self, endpoint: str) -> dict:
        url = f"{self.base_url}/{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"apikey": self.api_key}) as response:
                return await response.json()

    async def get_number(self) -> Optional[str]:
        try:
            response = await self._make_request(
                f"activation/number/{self.country}/{self.service}"
            )
            if response.get("status") == "success":
                self.current_order_id = response.get("id")
                return response.get("phone")
            return None
        except Exception as e:
            print(f"Error getting number: {str(e)}")
            return None

    async def get_sms_code(self, max_attempts: int = 12) -> Optional[str]:
        if not self.current_order_id:
            return None

        for attempt in range(max_attempts):
            try:
                response = await self._make_request(
                    f"activation/sms/{self.current_order_id}"
                )
                if response.get("status") == "success":
                    return response.get("sms")
                
                # Wait 5 seconds between attempts (as per API docs)
                await asyncio.sleep(5)
            except Exception as e:
                print(f"Error getting SMS code (attempt {attempt + 1}): {str(e)}")
        
        return None

class OutlookAuthenticator:
    def __init__(self, sms_pva_api_key: str):
        self.sms_pva = SMSPVAClient(sms_pva_api_key)
        self.max_retries = 3

    async def _handle_sms_verification(self, page) -> bool:
        try:
            # Check if SMS verification is needed
            if await page.is_visible('text="Verify"'):
                for attempt in range(self.max_retries):
                    # Get phone number from SMS PVA
                    phone_number = await self.sms_pva.get_number()
                    if not phone_number:
                        print(f"Failed to get phone number, attempt {attempt + 1}")
                        continue

                    # Enter phone number
                    await page.fill('input[placeholder="Phone number"]', phone_number)
                    await page.click('text="Send code"')

                    # Get verification code from SMS PVA
                    code = await self.sms_pva.get_sms_code()
                    if code:
                        # Enter verification code
                        await page.fill('input[aria-label="Code"]', code)
                        await page.press('input[aria-label="Code"]', "Enter")
                        
                        # Check if verification was successful
                        try:
                            await page.wait_for_selector('text="Outlook"', timeout=5000)
                            return True
                        except PlaywrightTimeoutError:
                            print(f"Verification failed with code: {code}")
                            # Go back if verification failed
                            try:
                                await page.go_back()
                            except:
                                pass
                            continue
                    
                    print(f"Failed to get SMS code, attempt {attempt + 1}")
                
                return False
            return True  # No SMS verification needed
        except Exception as e:
            print(f"SMS verification error: {str(e)}")
            return False

    async def login_to_outlook(self, page, email: str, password: str) -> bool:
        try:
            print(f"\nAttempting Outlook login for: {email}")
            
            # Navigate to Outlook with retry logic
            for attempt in range(self.max_retries):
                try:
                    await page.goto("https://go.microsoft.com/fwlink/p/?LinkID=2125442&deeplink=owa%2F", timeout=120000)
                    await page.wait_for_load_state("networkidle", timeout=120000)
                    break
                except Exception as e:
                    print(f"Outlook navigation attempt {attempt + 1} failed: {str(e)}")
                    if attempt == self.max_retries - 1:
                        return False
                    await asyncio.sleep(5)

            # Fill email
            await page.fill('input[type="email"]', email)
            await asyncio.sleep(random.uniform(1, 2))
            await page.click('input[type="submit"]')
            await page.wait_for_load_state("networkidle", timeout=60000)

            # Fill password
            await page.fill('input[type="password"]', password)
            await asyncio.sleep(random.uniform(1, 2))
            await page.click('input[type="submit"]')
            await page.wait_for_load_state("networkidle", timeout=60000)

            # Check for successful login
            try:
                await page.wait_for_selector('div[role="main"]', timeout=30000)
                print("Successfully logged into Outlook")
                
                # Look for verification email
                await page.wait_for_selector('input[aria-label="Search"]', timeout=30000)
                await page.fill('input[aria-label="Search"]', 'Instagram')
                await page.press('input[aria-label="Search"]', 'Enter')
                await page.wait_for_load_state("networkidle", timeout=60000)
                
                # Take screenshot for debugging
                await page.screenshot(path=f"outlook_search_{email}.png")
                
                return True
            except Exception as e:
                print(f"Error after login: {str(e)}")
                await page.screenshot(path=f"outlook_error_{email}.png")
                return False

        except Exception as e:
            print(f"Outlook login error: {str(e)}")
            await page.screenshot(path=f"outlook_exception_{email}.png")
            return False

class InstagramBatchLogin:
    def __init__(self, accounts_file: str, profile_ids_file: str, api_key: str, sms_pva_api_key: str):
        self.api_key = api_key
        self.accounts = self._load_accounts(accounts_file)
        self.profile_ids = self._load_profile_ids(profile_ids_file)
        self.login_results: Dict[str, str] = {}
        self.outlook_auth = OutlookAuthenticator(sms_pva_api_key)
        
    def _load_accounts(self, file_path: str) -> List[InstagramAccount]:
        accounts = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                account = InstagramAccount.from_line(line)
                if account:
                    accounts.append(account)
        if not accounts:
            raise ValueError("No valid accounts found in accounts file")
        return accounts

    def _load_profile_ids(self, file_path: str) -> List[str]:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f]

    async def _add_human_delay(self, page, min_delay=2000, max_delay=5000):
        delay = random.randint(min_delay, max_delay)
        await page.wait_for_timeout(delay)

    async def _handle_login_attempt(self, page, account: InstagramAccount) -> str:
        try:
            print(f"\nAttempting Instagram login for {account.username}")
            
            # First try Instagram login with retry logic
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    await page.goto("https://www.instagram.com/accounts/login/", timeout=120000)  # 2 minute timeout
                    await page.wait_for_load_state("networkidle", timeout=120000)
                    break
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {str(e)}")
                    if attempt == max_retries - 1:
                        raise
                    print("Retrying...")
                    await asyncio.sleep(5)  # Wait before retry
            
            # Login to Instagram with increased timeouts
            await page.fill('input[name="username"]', account.username, timeout=30000)
            await asyncio.sleep(random.uniform(1, 2))  # Longer delays for stability
            await page.fill('input[name="password"]', account.password, timeout=30000)
            await asyncio.sleep(random.uniform(1, 2))
            
            # Click submit and wait longer for response
            await page.click('button[type="submit"]')
            await page.wait_for_load_state("networkidle", timeout=120000)  # 2 minute timeout
            
            # Check for suspicious login attempt with longer timeout
            if await page.is_visible("text=We Detected An Unusual Login Attempt", timeout=30000):
                print("Suspicious login detected. Handling email verification...")
                await page.click("text=Continue", timeout=30000)
                await page.wait_for_load_state("networkidle", timeout=120000)
            
            # Check for verification code entry
            verification_selectors = [
                "text=Enter the code",
                "text=Security Code",
                "text=Enter the code we sent to",
                'input[name="verificationCode"]',
                'input[name="security_code"]'
            ]
            
            for selector in verification_selectors:
                if await page.is_visible(selector, timeout=30000):
                    print(f"Verification code required (matched: {selector}). Attempting Outlook login...")
                    await page.screenshot(path=f"instagram_verification_{account.username}.png")
                    
                    # Open new page for Outlook with retry logic
                    outlook_page = await page.context.new_page()
                    for attempt in range(max_retries):
                        try:
                            await outlook_page.goto(
                                "https://go.microsoft.com/fwlink/p/?LinkID=2125442&deeplink=owa%2F",
                                timeout=120000
                            )
                            await outlook_page.wait_for_load_state("networkidle", timeout=120000)
                            break
                        except Exception as e:
                            print(f"Outlook attempt {attempt + 1} failed: {str(e)}")
                            if attempt == max_retries - 1:
                                raise
                            print("Retrying Outlook connection...")
                            await asyncio.sleep(5)
                    
                    # Handle Outlook login
                    success = await self.outlook_auth.login_to_outlook(
                        outlook_page, 
                        account.email, 
                        account.email_password
                    )
                    
                    if success:
                        print("Successfully logged into Outlook")
                        await page.bring_to_front()
                        await asyncio.sleep(5)  # Longer wait for code to arrive
                        return "Verification Handled"
                    else:
                        print("Failed to log into Outlook")
                        return "Outlook Login Failed"
            
            # Check if login was successful
            if await page.is_visible('svg[aria-label="Home"]', timeout=60000):
                print("Successfully logged into Instagram")
                return "Success"
            else:
                print("Login failed - unknown error")
                await page.screenshot(path=f"instagram_error_{account.username}.png")
                return "Failed"
                
        except Exception as e:
            print(f"Error during login attempt: {str(e)}")
            await page.screenshot(path=f"instagram_exception_{account.username}.png")
            return f"Error: {str(e)}"

    async def process_batch(self, batch_size: int = 10):
        async with async_playwright() as p:
            active_browsers = []
            
            try:
                # Launch browsers for the batch
                for i in range(min(batch_size, len(self.profile_ids))):
                    if i >= len(self.accounts):
                        break
                        
                    profile_id = self.profile_ids[i]
                    query = urlencode({
                        'x-api-key': self.api_key,
                        'config': json.dumps({'headless': False, 'autoClose': False}),
                    })
                    
                    browser_ws_endpoint = f"ws://localhost:8848/devtool/launch/{profile_id}?{query}"
                    print(f"\nLaunching profile: {profile_id}")
                    
                    try:
                        browser = await p.chromium.connect_over_cdp(
                            browser_ws_endpoint,
                            timeout=60000
                        )
                        active_browsers.append((profile_id, browser, self.accounts[i]))
                    except Exception as e:
                        print(f"Failed to launch profile {profile_id}: {str(e)}")
                        continue

                # Process logins
                for profile_id, browser, account in active_browsers:
                    try:
                        page = browser.contexts[0].pages[0]
                        result = await self._handle_login_attempt(page, account)
                        self.login_results[account.username] = result
                    except Exception as e:
                        print(f"Error processing {account.username}: {str(e)}")
                        self.login_results[account.username] = f"Error: {str(e)}"

            finally:
                # Cleanup
                for _, browser, _ in active_browsers:
                    try:
                        await browser.close()
                    except:
                        pass

async def test_outlook_login():
    api_key = "9eb7357f-ed4b-45e7-beac-d0b1db34c2e4"
    sms_pva_api_key = "LVpUPRDNcr0nRVNVpsFOtYx5ucSAYG"
    
    async with async_playwright() as p:
        try:
            query = urlencode({
                'x-api-key': api_key,
                'config': json.dumps({'headless': False, 'autoClose': False}),
            })
            profile_id = "45cf7095-899b-45f4-b1e1-9d2e0e97db26"
            browser_ws_endpoint = f"ws://localhost:8848/devtool/launch/{profile_id}?{query}"
            
            browser = await p.chromium.connect_over_cdp(browser_ws_endpoint, timeout=60000)
            page = browser.contexts[0].pages[0]
            
            # Follow exact login sequence
            await page.goto("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=165&ct=1731535907&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26culture%3den-us%26country%3dus%26RpsCsrfState%3da5886aa3-3df8-ddb2-131f-f4de84bceff7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
            await page.wait_for_load_state("networkidle")
            
            # Enter email
            await page.get_by_test_id("i0116").click()
            await page.get_by_test_id("i0116").fill("ioykijxvr@hotmail.com")
            await page.get_by_test_id("i0116").press("Enter")
            await page.wait_for_load_state("networkidle")
            
            # Enter password
            await page.get_by_test_id("i0118").click()
            await page.get_by_test_id("i0118").fill("TVDJnh221")
            await page.get_by_test_id("i0118").press("Enter")
            await page.wait_for_load_state("networkidle")

            # Handle verification if needed
            try:
                verify_button = await page.get_by_role("button", name="Verify")
                if await verify_button.is_visible():
                    await verify_button.click()
                    await page.wait_for_load_state("networkidle")
                    
                    # Handle phone verification
                    phone_input = await page.get_by_placeholder("Phone number")
                    if await phone_input.is_visible():
                        # Get SMS number from API
                        print("Getting SMS number...")
                        # Add SMS PVA API call here
                        await phone_input.fill("smspvanumberhere")
                        await page.wait_for_load_state("networkidle")
                        
                        # Handle code entry
                        code_input = await page.get_by_label("Code", exact=True)
                        if await code_input.is_visible():
                            # Get SMS code from API
                            print("Waiting for SMS code...")
                            # Add SMS code retrieval here
                            await code_input.fill("123456")
                            await code_input.press("Enter")
                            await page.wait_for_load_state("networkidle")
            except Exception as e:
                print(f"Verification handling error: {e}")

            # Handle "Stay signed in?" prompt
            try:
                no_button = await page.get_by_role("button", name="No")
                if await no_button.is_visible():
                    await no_button.click()
            except:
                print("No 'Stay signed in' prompt found")

            print("Login sequence completed")
            await page.screenshot(path="outlook_final.png")
            await asyncio.sleep(30)  # Keep browser open to see result
            
        except Exception as e:
            print(f"Test error: {str(e)}")
        finally:
            try:
                await browser.close()
            except:
                pass

async def main():
    api_key = "9eb7357f-ed4b-45e7-beac-d0b1db34c2e4"  # NST Browser API key
    sms_pva_api_key = "LVpUPRDNcr0nRVNVpsFOtYx5ucSAYG"  # SMS PVA API key
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    accounts_file = os.path.join(base_dir, 'test_accounts.txt')
    profile_ids_file = os.path.join(base_dir, 'profile_ids.txt')
    
    print("Starting Instagram batch login test...")
    print(f"Using accounts file: {accounts_file}")
    print(f"Using profile IDs file: {profile_ids_file}")
    
    batch_login = InstagramBatchLogin(accounts_file, profile_ids_file, api_key, sms_pva_api_key)
    
    # Process just one account for testing
    async with async_playwright() as p:
        # Launch single browser for testing
        profile_id = batch_login.profile_ids[0]  # Get first profile
        account = batch_login.accounts[0]  # Get first account
        
        print(f"\nTesting with account: {account.username}")
        print(f"Using profile: {profile_id}")
        
        query = urlencode({
            'x-api-key': api_key,
            'config': json.dumps({'headless': False, 'autoClose': False}),
        })
        
        browser_ws_endpoint = f"ws://localhost:8848/devtool/launch/{profile_id}?{query}"
        print(f"\nLaunching profile: {profile_id}")
        
        try:
            browser = await p.chromium.connect_over_cdp(
                browser_ws_endpoint,
                timeout=60000
            )
            
            # Enable verbose logging
            page = browser.contexts[0].pages[0]
            
            # Start tracing for debugging
            await browser.contexts[0].tracing.start(
                screenshots=True,
                snapshots=True,
                sources=True
            )
            
            result = await batch_login._handle_login_attempt(page, account)
            print(f"\nLogin result: {result}")
            
            # Save trace for debugging
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            await browser.contexts[0].tracing.stop(
                path=f"trace_{timestamp}.zip"
            )
            
        except Exception as e:
            print(f"Error during test: {str(e)}")
        finally:
            try:
                await browser.close()
            except:
                pass

if __name__ == "__main__":
    asyncio.run(test_outlook_login())