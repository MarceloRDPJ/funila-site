from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()

        # Verify index.html
        print("Verifying index.html...")
        page.goto(f"file://{cwd}/index.html")

        # Check for favicon links
        # Note: Playwright selectors for attributes
        apple_touch = page.locator('link[rel="apple-touch-icon"]')
        favicon32 = page.locator('link[rel="icon"][sizes="32x32"]')
        favicon16 = page.locator('link[rel="icon"][sizes="16x16"]')

        if apple_touch.count() == 0:
            print("ERROR: index.html: apple-touch-icon not found")
        if favicon32.count() == 0:
            print("ERROR: index.html: favicon-32x32 not found")
        if favicon16.count() == 0:
            print("ERROR: index.html: favicon-16x16 not found")

        print("index.html favicon links checked.")
        page.screenshot(path="verification/index_verified.png")

        # Verify public/brandbook.html
        print("Verifying public/brandbook.html...")
        page.goto(f"file://{cwd}/public/brandbook.html")

        # Check for favicon links
        apple_touch = page.locator('link[rel="apple-touch-icon"]')
        favicon32 = page.locator('link[rel="icon"][sizes="32x32"]')
        favicon16 = page.locator('link[rel="icon"][sizes="16x16"]')

        if apple_touch.count() == 0:
            print("ERROR: brandbook.html: apple-touch-icon not found")
        if favicon32.count() == 0:
            print("ERROR: brandbook.html: favicon-32x32 not found")
        if favicon16.count() == 0:
            print("ERROR: brandbook.html: favicon-16x16 not found")

        print("brandbook.html favicon links checked.")
        page.screenshot(path="verification/brandbook_verified.png")

        browser.close()

if __name__ == "__main__":
    run()
