
def clean_item(item):
    # Title -> remove '®'
    title = item['title']
    item['title'] = title.replace('®', '')

    # Tags -> a list of tags 
    tags = item['tags'].split(',')
    item['tags'] = tags

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

    