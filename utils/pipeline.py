
from datetime import datetime
import re


def regex(text: str, pattern: str):
    r = re.compile(pattern)
    matches = r.findall(text)
    return matches


def get_first_five_tags(tags: list):
    return tags[:5]


def reformat_datetime(date: str, input_format="%b %d, %Y", output_format="%Y-%m-%d"):
    dt_obj = datetime.strptime(date, input_format)
    reformmatted_date = dt_obj.strftime(output_format)
    return reformmatted_date


def transform_review_to_int(reviews: str):
    reviews_str = reviews.split()[-1]
    reviews_int = int(reviews_str.replace(',',''))
    return reviews_int


def transform_price_to_float(price: str):
    price_str = price.split()[-1]
    price_float = float(price_str.replace(',',''))
    return price_float


def transform_discount_percentage_to_int(discount: str):
    return int(discount.strip('-').strip('%'))



def clean_item(item: dict):

    # When speaking of simple transformation, we should first think about tranformation table, a dictionary
    # Transfromation mapping 
    transformation = {
        "title": lambda title: " ".join(regex(title, r"[^®\s]+")),
        "tags": lambda tags: get_first_five_tags(tags),
        "release_date": lambda date: reformat_datetime(date),
        "num_reviews": lambda reviews: int("".join(regex(reviews, r"\d+"))),
        "original_price": lambda price: float(regex(price, r"\d+.\d{2}")),
        "discount % off": lambda discount: int(regex(discount, r"\d+"))

    }

    for key, value in transformation.items():
        if key in item:
            item[key] = value(item[key])


    return item



if __name__ == '__main__': 
    reformat_datetime()

    