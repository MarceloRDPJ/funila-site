from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 1200})

        cwd = os.getcwd()

        # Verify index.html Typography and Nav
        print("Verifying index.html...")
        page.goto(f"file://{cwd}/index.html")

        # Check nav
        nav = page.locator('nav')
        if nav.is_visible():
            print("Navigation is visible.")
            brand_btn = page.locator('a:text("Conheça a Marca")')
            if brand_btn.is_visible():
                print("Conheça a Marca button is visible.")
            else:
                print("ERROR: Conheça a Marca button not found in nav.")
        else:
            print("ERROR: Navigation not found.")

        # Check font size of body
        # We can't easily check computed style in python without JS eval, but visual check is key.
        # Let's take a screenshot of the Hero section text to see the font size and readability.
        page.locator('.hero-text-section').screenshot(path="verification/index_typography.png")
        print("Captured index_typography.png")

        # Verify public/brandbook.html Typography and Nav
        print("Verifying public/brandbook.html...")
        page.goto(f"file://{cwd}/public/brandbook.html")

        # Check nav back button
        home_btn = page.locator('a:text("Voltar ao Início")')
        if home_btn.is_visible():
            print("Voltar ao Início button is visible.")
        else:
            print("ERROR: Voltar ao Início button not found in brandbook nav.")

        # Screenshot typography
        page.locator('.hero').screenshot(path="verification/brandbook_typography.png")
        print("Captured brandbook_typography.png")

        browser.close()

if __name__ == "__main__":
    run()
