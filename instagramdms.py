import csv
import json
import os
import asyncio
import random
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from urllib.parse import urlencode

class InstagramDMAutomation:
    def __init__(self, csv_file, username_column, message_column, account_name, profile_id, api_key):
        self.csv_file = csv_file
        self.username_column = username_column
        self.message_column = message_column
        self.account_name = account_name
        self.profile_id = profile_id
        self.api_key = api_key
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    async def connect_to_nst_browser(self):
        host = 'localhost:8848'
        config = {
            'headless': False,
            'autoClose': False,
        }

        query = urlencode({
            'x-api-key': self.api_key,
            'config': json.dumps(config),
        })

        browser_ws_endpoint = f"ws://{host}/devtool/launch/{self.profile_id}?{query}"
        print(f'Launching profile: {self.profile_id}')

        self.browser = await self.playwright.chromium.connect_over_cdp(browser_ws_endpoint)
        self.context = self.browser.contexts[0]
        self.page = self.context.pages[0]

    async def load_session(self):
        await self.page.goto("https://www.instagram.com/")
        if "login" not in self.page.url:
            print("Session loaded successfully")
            return True
        else:
            print("Session expired or invalid")
            return False

    async def send_dms(self):
        with open(self.csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read the header row
            
            # Determine if we're using numeric indices or column names
            use_numeric = self.username_column.isdigit() and self.message_column.isdigit()
            
            if use_numeric:
                username_index = int(self.username_column) - 1
                message_index = int(self.message_column) - 1
            else:
                username_index = headers.index(self.username_column)
                message_index = headers.index(self.message_column)
            
            for row in csv_reader:
                username = row[username_index]
                message = row[message_index]
                await self.send_dm(username, message)

    async def send_dm(self, username, message):
        try:
            # Only navigate to inbox if we're not already there
            if "direct/inbox" not in self.page.url:
                await self.page.goto("https://www.instagram.com/direct/inbox/")
                await asyncio.sleep(random.uniform(3, 5))

            # Click "New message" button
            new_message_button = self.page.get_by_role("button", name="New message")
            await new_message_button.click()
            await asyncio.sleep(random.uniform(1, 2))

            # Wait for the search box to appear in the new message dialog
            search_box = self.page.get_by_placeholder("Search...")
            await search_box.wait_for()
            await search_box.click()
            await asyncio.sleep(random.uniform(0.5, 1))

            # Type username with human-like delays
            for char in username:
                await search_box.type(char, delay=random.uniform(100, 300))
                await asyncio.sleep(random.uniform(0.1, 0.3))

            await asyncio.sleep(random.uniform(1, 2))

            # Simple selector for username
            selector = f'div[role="dialog"] div[role="button"]:has-text("{username}")'
            username_element = await self.page.wait_for_selector(selector, timeout=5000)
            
            if username_element:
                await username_element.click()
                await asyncio.sleep(random.uniform(1, 2))

                # Click the "Chat" button
                chat_button = self.page.get_by_role("button", name="Chat")
                await chat_button.wait_for()
                await chat_button.click()
                await asyncio.sleep(random.uniform(1, 2))

                # Find and click the message input field
                message_box = self.page.get_by_label("Message", exact=True)
                await message_box.wait_for()
                await message_box.click()

                # Type message with human-like delays
                for char in message:
                    await message_box.type(char, delay=random.uniform(50, 200))
                    await asyncio.sleep(random.uniform(0.05, 0.2))

                await asyncio.sleep(random.uniform(1, 2))
                await self.page.keyboard.press("Enter")

                await asyncio.sleep(5)
                print(f"Successfully sent DM to {username}")
            else:
                print(f"User {username} not found in search results")

        except PlaywrightTimeoutError:
            print(f"User {username} not found in search results")
        except Exception as e:
            print(f"Unexpected error sending DM to {username}: {str(e)}")
        finally:
            # Clear search box and close dialog
            search_box = self.page.get_by_placeholder("Search...")
            if await search_box.is_visible():
                await search_box.fill("")
            
            close_button = self.page.get_by_role("button", name="Close")
            if await close_button.is_visible():
                await close_button.click()
            
            await asyncio.sleep(random.uniform(1, 2))

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

async def main():
    account_name = input("Enter your Instagram account name: ")
    csv_file = input("Enter the path to your CSV file: ")
    username_column = input("Enter the column name for usernames: ")
    message_column = input("Enter the column name for messages: ")
    profile_id = input("Enter your NST Browser profile ID: ")
    api_key = input("Enter your NST Browser API key: ")

    async with async_playwright() as playwright:
        automation = InstagramDMAutomation(csv_file, username_column, message_column, account_name, profile_id, api_key)
        automation.playwright = playwright

        await automation.connect_to_nst_browser()

        if await automation.load_session():
            await automation.send_dms()
        else:
            print("Failed to load session. Please check your NST Browser profile.")

        await automation.close()

if __name__ == "__main__":
    asyncio.run(main())