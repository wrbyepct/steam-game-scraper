_config = {
    "url": "https://store.steampowered.com/specials",
    "meta": {
        "name": "Steam Sales Scraper",
        "description": "Extracts the highest discounted games from Steam",
        "author": "Jay Hong",
        "version": "0.1.1"
    },
    "container": [
        {
            "parent_container": "div[class*='facetedbrowse_FacetedBrowseInnerCtn']",
            "name": "store_sale_divs",
            "selector": "div[class*='salepreviewwidgets_SaleItemBrowserRow']",
            "match": "all",
            "type": "node",
            "item": [
                {
                    "name": "title",
                    "selector": "div[class*='StoreSaleWidgetTitle']",
                    "match": "first",
                    "type": "text" 
                },
                {
                    "name": "thumbnail",
                    "selector": "img[class*='salepreviewwidgets_CapsuleImage']",
                    "match": "first",
                    "type": "src"
                },
                {
                
                    "name": "tags",
                    "selector": "div[class*='salepreviewwidgets_StoreSaleWidgetTags'] a",
                    "match": "all",
                    "type": "text"
                },
                {
                    "name": "release_date",
                    "selector": "div[class*=salepreviewwidgets_StoreSaleWidgetRelease_]",
                    "match": "first",
                    "type": "text"
                },
                {
                    "name": "rating",
                    "selector": "div[class*='gamehover_ReviewScoreValue'] > div",
                    "match": "first",
                    "type": "text"
                },
                {
                    "name": "num_reviews",
                    "selector": "div[class*='gamehover_ReviewScoreCount_']",
                    "match": "first",
                    "type": "text"
                },
                {
                    "name": "original_price NTD",
                    "selector": "div[class*='salepreviewwidgets_StoreOriginalPrice_']",
                    "match": "first",
                    "type": "text"
                },
                {
                    "name": "sale_price NTD",
                    "selector": "div[class*='salepreviewwidgets_StoreSalePriceBox']",
                    "match": "first",
                    "type": "text"
                },
                {
                    "name": "discount % off",
                    "selector": "div[class*='salepreviewwidgets_StoreSaleDiscountBox_']",
                    "match": "first",
                    "type": "text"
                }

            ]
        }
    ]
    
}

import json 

def get_config(load_from_file=False):
    if load_from_file:
        with open ("config.json", "r") as f:
            return json.load(f)
    return _config

def generate_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)


if __name__ == "__main__":
    generate_config()