
from datetime import datetime
def clean_item(item):
    # Title -> remove '®'
    title = item['title']
    item['title'] = title.replace('®', '')

    # Tags -> first 5
    item['tags'] = item['tags'][:5]

    # Release date -> 2022-12-12
    date_format = "%b %d, %Y"
    dt = datetime.strptime(item['release_date'], date_format)
    formatted_date = dt.strftime("%Y-%m-%d")
    item['release_date'] = formatted_date

    # number of reviews -> integer
    reivews_str = item['num_reviews'].split()[1]
    item['num_reviews'] = int(reivews_str.replace(',', ''))
    
    # price -> float 
    price = item['original_price'].split()[-1]
    item['original_price'] = float(price.replace(',',''))

    # discount -> integer
    discount_str = item["discount % off"].strip('-').strip('%')
    item["discount % off"] = int(discount_str)

    return item

    