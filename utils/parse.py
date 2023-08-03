from selectolax.parser import Node

def parse_raw_attibutes(node: Node, selectors: list):
    parsed = {}

    # For all the nodes passed in, I want the all the following attributes
    # ITEM WE NEED 
        # 1. title 
        # 2. link to thumbnail
        # 3. category tags
        # 4. relase date
        # 5. rating
        # Number reviews
        # Original price
        # Discount %
    for s in selectors:
        name = s.get('name')
        selector = s.get('selector')
        match  = s.get('match')
        type_ =  s.get('type')

        # Determine if it's a select all or first 
        if match == "all":
            # We either extract all nodes or texts from an item
            if type_ == "text":
                parsed[name] = [n.text() for n in node.css(selector)]
            else:
                parsed[name] = node.css(selector)
        else:
            if type_ == "src":
                parsed[name] = node.css_first(selector).attrs.get('src')
            elif type_ == "href":
                parsed[name] = node.css_first(selector).attrs.get('href')
            else:
                parsed[name] = node.css_first(selector).text()
    
    return parsed


