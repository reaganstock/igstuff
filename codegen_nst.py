import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlencode
import json
import argparse

async def launch_and_connect_to_browser(profile_id, codegen=False):
    host = 'localhost:8848'
    api_key = '9eb7357f-ed4b-45e7-beac-d0b1db34c2e4'
    config = {
        'headless': False,
        'autoClose': False,
    }

    query = urlencode({
        'x-api-key': api_key,
        'config': json.dumps(config),
    })

    browser_ws_endpoint = f"ws://{host}/devtool/launch/{profile_id}?{query}"
    print(f'Launching profile: {profile_id}')

    await exec_playwright(browser_ws_endpoint, codegen)

async def exec_playwright(browser_ws_endpoint, codegen):
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(browser_ws_endpoint)
        context = browser.contexts[0]
        
        # Start tracing before creating / navigating a page
        await context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )
        
        page = context.pages[0]
        
        if codegen:
            await page.goto('about:blank')  # Start with a blank page for codegen
            await page.pause()  # This will start the codegen session
        else:
            await page.goto('https://google.com')
            await page.wait_for_load_state()
        
        try:
            input("Press Enter to Exit")
        finally:
            # Stop tracing and save to file with timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            await context.tracing.stop(
                path=f"trace_{timestamp}.zip"
            )

async def launch_multiple_profiles(profile_ids, codegen):
    tasks = [launch_and_connect_to_browser(profile_id, codegen) for profile_id in profile_ids]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Instagram automation with optional codegen.")
    parser.add_argument("--codegen", action="store_true", help="Run in codegen mode")
    args = parser.parse_args()

    profile_ids = [
    '8e1deb06-627f-4ac0-aa49-27de8fb0237b',
    ]

    asyncio.run(launch_multiple_profiles(profile_ids, args.codegen))