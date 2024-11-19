from playwright.sync_api import sync_playwright
import time
import re
import json
import logging
from typing import Dict, List, Optional, Tuple
import asyncio
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'instagram_login_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

class InstagramLoginManager:
    def __init__(self):
        self.accounts: List[Dict] = []
        self.current_account: Optional[Dict] = None
        self.browser = None
        self.context = None
        self.page = None
        
    def load_accounts(self, filename: str) -> None:
        """Load and parse Hotmail accounts from the accounts file."""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(':')
                    if len(parts) == 5 and '@hotmail.com' in parts[2]:
                        self.accounts.append({
                            'username': parts[0],
                            'ig_password': parts[1],
                            'email': parts[2],
                            'email_password': parts[3],
                            'year': parts[4],
                            'status': 'pending'
                        })
            logging.info(f"Loaded {len(self.accounts)} Hotmail accounts")
        except Exception as e:
            logging.error(f"Error loading accounts: {str(e)}")
            raise

    async def login_to_outlook(self, email: str, password: str) -> bool:
        """
        Login to Outlook to access verification codes.
        This will be replaced with your Playwright codegen code.
        """
        # TODO: Replace with your Playwright codegen code for Outlook login
        logging.info(f"Attempting to log into Outlook for {email}")
        return True

    async def login_to_instagram(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Login to Instagram.
        This will be replaced with your Playwright codegen code.
        Returns: (success: bool, status: str)
        """
        # TODO: Replace with your Playwright codegen code for Instagram login
        logging.info(f"Attempting to log into Instagram for {username}")
        return True, "success"

    async def get_verification_code(self) -> Optional[str]:
        """
        Extract verification code from Outlook email.
        This will be replaced with your Playwright codegen code.
        """
        # TODO: Replace with your Playwright codegen code for extracting verification code
        return None

    async def process_account(self, account: Dict) -> None:
        """Process a single account login attempt."""
        self.current_account = account
        logging.info(f"Processing account: {account['username']}")
        
        try:
            # First attempt Instagram login
            success, status = await self.login_to_instagram(
                account['username'], 
                account['ig_password']
            )

            if not success and "verification_required" in status:
                # If verification needed, login to Outlook
                outlook_success = await self.login_to_outlook(
                    account['email'],
                    account['email_password']
                )
                
                if outlook_success:
                    # Get verification code
                    code = await self.get_verification_code()
                    if code:
                        # TODO: Add your code for entering verification code
                        pass

            account['status'] = status
            logging.info(f"Account {account['username']} processed. Status: {status}")
            
        except Exception as e:
            account['status'] = f"error: {str(e)}"
            logging.error(f"Error processing account {account['username']}: {str(e)}")

    async def process_all_accounts(self) -> None:
        """Process all loaded accounts."""
        for account in self.accounts:
            await self.process_account(account)
            # Add random delay between accounts
            await asyncio.sleep(2)  # Adjust delay as needed

    def save_results(self, filename: str) -> None:
        """Save processing results to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.accounts, f, indent=2)
            logging.info(f"Results saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving results: {str(e)}")

async def main():
    manager = InstagramLoginManager()
    manager.load_accounts('accounts.txt')
    
    async with sync_playwright() as p:
        # Set up browser - you can modify these settings as needed
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        manager.browser = browser
        manager.context = context
        manager.page = page
        
        await manager.process_all_accounts()
        manager.save_results('login_results.json')

if __name__ == "__main__":
    asyncio.run(main())
