import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlencode
import json
import time

async def test_login():
    api_key = "9eb7357f-ed4b-45e7-beac-d0b1db34c2e4"
    
    async with async_playwright() as p:
        try:
            query = urlencode({
                'x-api-key': api_key,
                'config': json.dumps({'headless': False, 'autoClose': False}),
            })
            profile_id = "fd62f06e-f01a-45cc-855e-3d287839d7c3"
            browser_ws_endpoint = f"ws://localhost:8848/devtool/launch/{profile_id}?{query}"
            
            browser = await p.chromium.connect_over_cdp(browser_ws_endpoint, timeout=60000)
            page = browser.contexts[0].pages[0]
            
            # Start with the account recovery URL
            recovery_url = "https://account.live.com/recover?mkt=EN-US&uiflavor=web&id=292841&lmif=80&ru=https://login.live.com/login.srf%3fid%3d292841%26opid%3d07AF04215D2A7D29%26opidt%3d1731541373"
            await page.goto(recovery_url)
            await page.wait_for_load_state("networkidle")
            await page.screenshot(path=f"step1_recovery_{time.time()}.png")
            
            # Fill email
            await page.locator("#i0116").fill("ioykijxvr@hotmail.com")
            await asyncio.sleep(1)
            await page.keyboard.press("Enter")
            await page.wait_for_load_state("networkidle")
            await page.screenshot(path=f"step2_after_email_{time.time()}.png")
            
            # Look for and click "Add a phone number" option
            try:
                add_phone_selectors = [
                    "text=Add a phone number",
                    '[data-bind*="phoneNumber"]',
                    "button:has-text('Add phone')",
                    '[aria-label*="phone"]'
                ]
                
                for selector in add_phone_selectors:
                    try:
                        element = await page.wait_for_selector(selector, timeout=5000)
                        if element:
                            print(f"Found add phone element: {selector}")
                            await element.click()
                            await page.wait_for_load_state("networkidle")
                            await page.screenshot(path=f"step3_phone_click_{time.time()}.png")
                            break
                    except Exception as e:
                        print(f"Add phone selector {selector} not found: {str(e)}")
                
                # Now handle phone number input
                phone_input_selectors = [
                    "input[placeholder*='Phone']",
                    "input[type='tel']",
                    "#PhoneNumber",
                    '[aria-label*="Phone"]'
                ]
                
                for selector in phone_input_selectors:
                    try:
                        phone_input = await page.wait_for_selector(selector, timeout=5000)
                        if phone_input:
                            print(f"Found phone input: {selector}")
                            await phone_input.fill("1234567890")  # Replace with SMS PVA number
                            await page.screenshot(path=f"step4_phone_filled_{time.time()}.png")
                            await page.keyboard.press("Enter")
                            await page.wait_for_load_state("networkidle")
                            break
                    except Exception as e:
                        print(f"Phone input selector {selector} not found: {str(e)}")
                
                # Handle verification code
                code_selectors = [
                    "input[placeholder*='Code']",
                    "#idTxtBx_SAOTCC_OTC",
                    '[aria-label="Enter the code"]',
                    "input[type='text']"
                ]
                
                for selector in code_selectors:
                    try:
                        code_input = await page.wait_for_selector(selector, timeout=5000)
                        if code_input:
                            print(f"Found code input: {selector}")
                            await code_input.fill("123456")  # Replace with actual SMS code
                            await page.screenshot(path=f"step5_code_filled_{time.time()}.png")
                            await page.keyboard.press("Enter")
                            await page.wait_for_load_state("networkidle")
                            break
                    except Exception as e:
                        print(f"Code input selector {selector} not found: {str(e)}")
                
            except Exception as e:
                print(f"Recovery flow error: {str(e)}")
                await page.screenshot(path=f"error_{time.time()}.png")
            
            # Keep browser open to see what's happening
            await asyncio.sleep(60)
            
        except Exception as e:
            print(f"Test error: {str(e)}")
            await page.screenshot(path=f"final_error_{time.time()}.png")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(test_login())
