from selectolax.parser import HTMLParser
import json
from extract_html import get_html_body
from pipeline import clean_item
import pandas as pd

        # ITEM WE NEED 
        # 1. title 
        # 2. link to thumbnail
        # 3. category tags
        # 4. rating
        # Number reviews
        # Original price
        # Discount %


def scrape_games(html):
    tree = HTMLParser(html)

    with open('config.json', "r") as f:
        css = json.load(f)
  
    items = tree.css(css['item'])
    games = []
    for item in items:
        game = {}
        title = item.css_first(css['title']).text()
        thumbnail = item.css_first(css['thumbnail']).attrs.get('src') 
        tags = item.css_first(css['tags']).text(separator=",") 
        rating = item.css_first(css['rating']).text(deep=False) 
        num_reviews = item.css_first(css['num_reviews']).text() 
        price = item.css_first(css['price']).text()
        discount = item.css_first(css['discount']).text() 

        game = {
            "title": title,
            "thumbnail": thumbnail,
            "tags": tags,
            "rating": rating,
            "num_reviews": num_reviews,
            "original_price": price,
            "discount % off": discount
        }

        clean_game = clean_item(game)
        games.append(clean_game)

    return games


if __name__ == '__main__':
    url = "https://store.steampowered.com/specials"
    html = get_html_body(url)
    games = scrape_games(html)
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(games)
    df.to_csv('discount-games.csv', index=False)
    print(df)
