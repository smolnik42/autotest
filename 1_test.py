from playwright.sync_api import Playwright, sync_playwright


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com/")

    search_box = page.locator('[name="q"]')
    search_box.click()
    search_box.fill('sql')
    search_box.press('Enter')

    page.wait_for_selector('#search', timeout=10000)

    context.close()
    browser.close()


