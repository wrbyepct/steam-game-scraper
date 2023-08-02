from playwright.sync_api import sync_playwright
from css_select import CSS

def get_html_body(url):

    TIMEOUT = 90000 #ms
    # Set upt broswer, specify browser 
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        
        # Wait for JavaScript loading 
        page.wait_for_load_state('networkidle', timeout=TIMEOUT)
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        page.wait_for_selector(f'{CSS.GAME_COLUMN_SELECTOR}', timeout=TIMEOUT)
        

        return page.inner_html('body')


