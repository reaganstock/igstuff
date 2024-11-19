import asyncio
import json
import random
import re
import time
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from urllib.parse import urlencode

class InstagramAutomation:
    def __init__(self, config, profile_id, api_key):
        self.config = config
        self.profile_id = profile_id
        self.api_key = api_key
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    async def connect_to_nst_browser(self):
        query = urlencode({
            'x-api-key': self.api_key,
            'config': json.dumps({'headless': False, 'autoClose': False}),
        })
        browser_ws_endpoint = f"ws://localhost:8848/devtool/launch/{self.profile_id}?{query}"
        print(f'Launching profile: {self.profile_id}')
        self.browser = await self.playwright.chromium.connect_over_cdp(browser_ws_endpoint)
        self.context = self.browser.contexts[0]
        self.page = self.context.pages[0]

    async def load_session(self):
        await self.page.goto("https://www.instagram.com/")
        return "login" not in self.page.url

    async def perform_action(self, action_func):
        try:
            await action_func()
            print(f"{action_func.__name__} completed successfully")
        except Exception as e:
            print(f"Error in {action_func.__name__}: {str(e)}")

    async def delete_content(self):
        async def delete_items(content_type):
            print(f"Deleting {content_type}...")
            await asyncio.sleep(random.uniform(5, 7))
            while True:
                select_button = self.page.get_by_role("button", name="Select")
                if not await select_button.is_visible(timeout=5000):
                    print(f"No more {content_type} to delete")
                    return
                await select_button.click()
                await asyncio.sleep(random.uniform(0.5, 1))
                checkboxes = self.page.get_by_label("Toggle checkbox")
                checkbox_count = await checkboxes.count()
                if checkbox_count == 0:
                    print(f"No {content_type} to delete")
                    return
                for i in range(checkbox_count):
                    await checkboxes.nth(i).click()
                    await asyncio.sleep(random.uniform(0.3, 0.5))
                delete_button = self.page.get_by_role("button", name="Delete", exact=True)
                if await delete_button.is_visible(timeout=5000):
                    await delete_button.click()
                    await asyncio.sleep(random.uniform(0.5, 1))
                    confirm_delete = self.page.get_by_role("button", name="Delete")
                    if await confirm_delete.is_visible(timeout=5000):
                        await confirm_delete.click()
                        await asyncio.sleep(random.uniform(2, 3))
                        print(f"Deleted {checkbox_count} {content_type}")
                    else:
                        print(f"Confirm delete button not found for {content_type}")
                else:
                    print(f"Delete button not found for {content_type}")

        await self.page.goto("https://www.instagram.com/")
        await self.page.get_by_role("link", name="Settings More").click()
        await asyncio.sleep(random.uniform(1, 2))
        await self.page.get_by_role("link", name="Your activity Your activity").click()
        await asyncio.sleep(random.uniform(1, 2))
        await self.page.get_by_role("link", name="Photos and videos, view,").click()
        await asyncio.sleep(random.uniform(1, 2))

        for content_type in ["posts", "reels", "highlights"]:
            if content_type != "posts":
                await self.page.get_by_role("tab", name=content_type.capitalize()).click()
                await asyncio.sleep(random.uniform(3, 5))
            await delete_items(content_type)

    async def update_profile(self):
        await self.page.goto("https://accountscenter.instagram.com/?entry_point=app_settings", timeout=60000)
        await asyncio.sleep(random.uniform(2, 3))
        await self.page.get_by_label("darren.ross42 Instagram").click()
        await asyncio.sleep(random.uniform(2, 3))

        updates = self.config['profile_updates']

        async def update_field(field):
            if updates.get(f'change_{field}'):
                await self.page.get_by_label(field.capitalize(), exact=True).click()
                await asyncio.sleep(random.uniform(1, 2))
                await self.page.get_by_label(field.capitalize()).fill(updates[f'new_{field}'])
                await asyncio.sleep(random.uniform(1, 2))
                done_button = self.page.get_by_role("button", name="Done")
                back_button = self.page.get_by_role("button", name="Back")
                
                if await done_button.is_enabled():
                    await done_button.click()
                    await asyncio.sleep(random.uniform(2, 3))
                    if await self.page.get_by_label("Name", exact=True).is_visible() and \
                       await self.page.get_by_label("Username", exact=True).is_visible():
                        print(f"{field.capitalize()} update successful")
                    else:
                        print(f"{field.capitalize()} update unsuccessful")
                        await back_button.click()
                else:
                    await back_button.click()
                    print(f"{field.capitalize()} update not allowed at this time")
                
                await asyncio.sleep(random.uniform(2, 3))

        for field in ['name', 'username']:
            await update_field(field)

        if updates.get('change_profile_pic'):
            await self.page.get_by_label("Profile picture").click()
            await asyncio.sleep(random.uniform(1, 2))
            upload_button = self.page.get_by_role("button", name="Upload new photo")
            if await upload_button.is_visible():
                file_input = await self.page.query_selector('input[type="file"]')
                await file_input.set_input_files(updates['profile_pic_path'])
                await asyncio.sleep(random.uniform(1, 2))
                save_button = self.page.get_by_role("button", name="Save")
                if await save_button.is_enabled():
                    await save_button.click()
                await asyncio.sleep(random.uniform(5, 7))
                print("Profile picture updated")
            else:
                print("Upload button not found")

        await self.page.goto("https://www.instagram.com/accounts/edit")
        await asyncio.sleep(random.uniform(2, 3))
        
        if updates.get('change_bio'):
            current_bio = await self.page.get_by_placeholder("Bio").input_value()
            if current_bio != updates['new_bio']:
                await self.page.get_by_placeholder("Bio").fill(updates['new_bio'])
                await asyncio.sleep(random.uniform(1, 2))
                submit_button = self.page.get_by_role("button", name="Submit")
                if await submit_button.is_enabled():
                    await submit_button.click()
                    await asyncio.sleep(random.uniform(2, 3))
                    print("Bio updated")
            else:
                print("Bio unchanged, skipping update")

    async def create_posts(self):
        for index, post in enumerate(self.config['posts'], 1):
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    print(f"Creating post/reel {index} of {len(self.config['posts'])} (Attempt {attempt + 1})")
                    await self.page.goto("https://www.instagram.com/")
                    await asyncio.sleep(random.uniform(2, 3))
                    
                    await self.page.get_by_role("link", name="New post").click(timeout=10000)
                    print("Clicked Create button")
                    await asyncio.sleep(random.uniform(2, 3))
                    
                    await self.page.wait_for_selector('a[role="link"]:has-text("Post")', timeout=15000)
                    print("Post option appeared")
                    
                    await self.page.get_by_role("link", name="Post Post").click(timeout=10000)
                    print("Clicked Post option")
                    
                    await asyncio.sleep(random.uniform(2, 3))
                    
                    file_input = await self.page.query_selector('input[type="file"]')
                    await file_input.set_input_files(post['media_paths'])
                    await asyncio.sleep(random.uniform(2, 3))
                    
                    for _ in range(2):
                        await self.page.get_by_role("button", name="Next").click(timeout=10000)
                        await asyncio.sleep(random.uniform(1, 2))
                    
                    await self.page.get_by_label("Write a caption...").fill(post['caption'])
                    await asyncio.sleep(random.uniform(1, 2))
                    
                    if 'location' in post:
                        await self.page.get_by_placeholder("Add location").fill(post['location'])
                        await asyncio.sleep(random.uniform(1, 2))
                        await self.page.get_by_role("button", name=post['location'], exact=True).first.click(timeout=10000)
                        await asyncio.sleep(random.uniform(1, 2))
                    
                    if 'alt_text' in post:
                        await self.page.get_by_role("button", name="Accessibility Down chevron").click(timeout=10000)
                        await asyncio.sleep(random.uniform(1, 2))
                        await self.page.get_by_placeholder("Write alt text...").fill(post['alt_text'])
                        await asyncio.sleep(random.uniform(1, 2))
                    
                    await self.page.get_by_role("button", name="Advanced settings Down").click(timeout=10000)
                    await asyncio.sleep(random.uniform(1, 2))
                    
                    switches = self.page.get_by_role("switch")
                    if post.get('hide_likes_views', False):
                        await switches.nth(1).check()
                    if post.get('disable_comments', False):
                        await switches.nth(2).check()
                    if not post.get('share_to_threads', True):
                        await switches.nth(3).uncheck()
                    
                    await self.page.get_by_role("button", name="Share").click(timeout=10000)
                    
                    start_time = time.time()
                    shared = False
                    while time.time() - start_time < 122:
                        try:
                            spinner = self.page.get_by_role("img", name="Spinner placeholder")
                            if await spinner.is_visible(timeout=1000):
                                print("Post/Reel is still uploading...")
                                await asyncio.sleep(5)
                                continue
                            
                            post_shared = self.page.get_by_text("Your post has been shared.")
                            reel_shared = self.page.get_by_text("Your reel has been shared.")
                            checkmark = self.page.get_by_role("img", name="Animated checkmark")
                            
                            if await post_shared.is_visible(timeout=1000) or \
                               await reel_shared.is_visible(timeout=1000) or \
                               await checkmark.is_visible(timeout=1000):
                                print(f"Post/Reel {index} confirmed shared.")
                                shared = True
                                break
                            
                            await asyncio.sleep(5)
                        except PlaywrightTimeoutError:
                            pass
                    
                    if shared:
                        close_button = self.page.get_by_role("button", name="Close")
                        if await close_button.is_visible(timeout=5000):
                            await close_button.click()
                        print(f"Successfully created post/reel {index}: {post['caption'][:20]}...")
                        break
                    else:
                        print(f"Timeout: Couldn't confirm if post/reel {index} was shared after 122 seconds. Status unknown.")
                    
                    await asyncio.sleep(random.uniform(1, 2))
                    
                except Exception as e:
                    print(f"Error creating post/reel {index} (Attempt {attempt + 1}): {str(e)}")
                    if attempt == max_retries - 1:
                        print(f"Failed to create post/reel {index} after {max_retries} attempts")
                
                if attempt < max_retries - 1:
                    await asyncio.sleep(random.uniform(10, 15))
            
            if index < len(self.config['posts']):
                await asyncio.sleep(random.uniform(10, 15))

    async def follow_users(self):
        for username in self.config['users_to_follow']:
            try:
                print(f"Attempting to follow user: {username}")
                await self.page.goto(f"https://www.instagram.com/{username}/", wait_until="networkidle")
                await asyncio.sleep(random.uniform(2, 3))

                if "Page Not Found" in await self.page.title():
                    print(f"Profile not found for user: {username}")
                    continue

                follow_button = None
                follow_selectors = [
                    "button:has-text('Follow'):not(:has-text('Following'))",
                    "[data-testid='user-profile-follow-button']",
                    "header button:has-text('Follow')",
                    "button:has-text('Follow')",
                ]

                for selector in follow_selectors:
                    follow_button = self.page.locator(selector).first
                    if await follow_button.is_visible(timeout=5000):
                        break

                if await follow_button.is_visible():
                    await follow_button.click()
                    await asyncio.sleep(random.uniform(1, 2))
                    
                    unfollow_button = self.page.get_by_role("button", name="Unfollow")
                    if await unfollow_button.is_visible(timeout=5000):
                        print(f"Already following user: {username}")
                    else:
                        print(f"Successfully followed user: {username}")
                else:
                    print(f"Couldn't find follow button for user: {username}")

            except Exception as e:
                print(f"Error processing user {username}: {str(e)}")
            
            await asyncio.sleep(random.uniform(5, 10))

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

async def main():
    with open('instagram_config.json', 'r') as config_file:
        config = json.load(config_file)

    profile_id = input("Enter your NST Browser profile ID: ")
    api_key = input("Enter your NST Browser API key: ")

    async with async_playwright() as playwright:
        automation = InstagramAutomation(config, profile_id, api_key)
        automation.playwright = playwright

        try:
            await automation.connect_to_nst_browser()
            if await automation.load_session():
                print("Successfully loaded Instagram session")
                
                actions = [
                    automation.delete_content,
                    automation.update_profile,
                    automation.create_posts,
                    automation.follow_users
                ]

                for action in actions:
                    await automation.perform_action(action)
                    await asyncio.sleep(random.uniform(5, 10))
            else:
                print("Failed to load Instagram session")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            await automation.close()

if __name__ == "__main__":
    asyncio.run(main())