from selectolax.parser import HTMLParser
from utils.extract import get_html
from utils.pipeline import clean_item, save_to_file
from utils.parse import parse_raw_attibutes
from config.tools import get_config

        # ITEM WE NEED 
        # 1. title 
        # 2. link to thumbnail
        # 3. category tags
        # 4. rating
        # Number reviews
        # Original price
        # Discount %


def scrape_games(html, config) -> list[dict]:
    tree = HTMLParser(html)

    # Get the item description we want to scrape
    # E.g All the divs that contain games
    # E.g What attribute we want to scrape from the item?
    #       i.e. price, title, discount, date, etc
    
    # For now we just have one container of concern
    container = parse_raw_attibutes(tree, config['container'])
    items = []
    # For every container we have specific attributes of interest from an item 
    for node in container['store_sale_divs']:
        ## Initial paring the item
        parsed = parse_raw_attibutes(node, config['container'][0]['item'])

        ## Clean the item in pipeline
        cleaned_item = clean_item(parsed)
        items.append(cleaned_item)

    return items


if __name__ == '__main__':
    config = get_config() 
    url = config['url']
    html = get_html(url, config)
    games = scrape_games(html, config)
    save_to_file(data=games)

    
    
