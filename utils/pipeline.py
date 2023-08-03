
from datetime import datetime
import re
import pandas as pd


def regex(text: str, pattern: str, method:str, sub=""):
    r = re.compile(pattern)
    if method == "findall":
        match = r.findall(text)
    elif method == "sub":
        match = r.sub(sub, text)
    elif method == "search":
        match = r.search(text).group()
    else:
        raise ValueError("A search method must be provided: findnall, replace")
    return match


def get_first_five_tags(tags: list):
    return tags[:5]


def reformat_datetime(date: str, input_format="%b %d, %Y", output_format="%Y-%m-%d"):
    dt_obj = datetime.strptime(date, input_format)
    reformmatted_date = dt_obj.strftime(output_format)
    return reformmatted_date


def clean_item(item: dict):

    # When speaking of simple transformation, we should first think about tranformation table, a dictionary
    # Transfromation mapping 
    transformation = {
        "title": lambda title: " ".join(regex(title, r"[^®\s]+", method="findall")),
        "tags": lambda tags: get_first_five_tags(tags),
        "release_date": lambda date: reformat_datetime(date),
        "num_reviews": lambda reviews: int("".join(regex(reviews, r"\d+", method="findall"))),
        "original_price NTD": lambda price: float("".join(regex(price, r"[^\d\.]", method="sub"))),
        "sale_price NTD": lambda price: float("".join(regex(price, r"[^\d\.]", method="sub"))),
        "discount % off": lambda discount: int(regex(discount, r"\d+", method="search"))
    }

    for key, value in transformation.items():
        if key in item:
            item[key] = value(item[key])


    return item


def save_to_file(filename="steam_games", data: list[dict]=None):
    if data is None:
        raise ValueError("Provided data is None, something went wrong.")
    # Display and save clean data
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(data)
    df.to_csv(f'{datetime.now().strftime("%Y_%m_%d")}_{filename}.csv', index=False)


if __name__ == '__main__': 
    reformat_datetime()

    