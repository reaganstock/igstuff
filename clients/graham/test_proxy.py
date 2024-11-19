from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        proxy={
            "server": "http://89.252.169.114:808",
            "username": "palfresh",
            "password": "palfresh"
        }
    )
    page = browser.new_page()
    try:
        page.goto("http://httpbin.org/ip")
        content = page.content()
        print(content)
    except Exception as e:
        print("Error:", str(e))
    browser.close()