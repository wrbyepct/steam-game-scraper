from playwright.sync_api import sync_playwright
from config import tools


def get_html_body(url):

    TIMEOUT = 90000 #ms
    # Set upt broswer, specify browser 
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # Wait for JavaScript loading 
        page.wait_for_load_state('networkidle', timeout=TIMEOUT)
        # Scroll down the window to make it load more content
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')

        config = tools.get_config()
        container = config['container'][0]
        page.wait_for_selector(container['selector'], timeout=TIMEOUT)

        # Return only the section of html we want
        game_rows_container = page.query_selector(container['parent_container'])
        return game_rows_container.inner_html()


