#! /usr/bin/python3

import pandas as pd
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time


## READ URLS TO ITER OVER -------------------------------------------------------

BASE_URL = "https://www.amazon.com/s?k=gound+coffee&tag=duckduckgo-20"

driver = webdriver.Chrome()
driver.get(BASE_URL)
time.sleep(5)

products = driver.find_elements_by_partial_link_text("Coffee")

urls = list(map(lambda x: x.get_attribute("href"), products))
driver.close()


## FOR EACH PRODUCT ----------------------------------------------------------------
def catnap():
    time.sleep(random.randint(1, 3))


def nap():
    time.sleep(random.randint(2, 5))


def page_iter(product, star):

    star = str(star)
    driver = webdriver.Chrome()

    # open url from list
    driver.get(product)
    catnap()

    review_link = driver.find_element_by_partial_link_text(
        "See all reviews from the United States"
    )
    review_link.click()

    review_type_dropdown = Select(
        driver.find_element_by_css_selector("#star-count-dropdown")
    )
    review_type_dropdown.select_by_visible_text(star + " star only")

    page = driver.find_element_by_css_selector("body")
    page.click()

    reviews = driver.find_elements_by_css_selector(".review-text-content span")

    # for i in reviews:
    #     print(i.text)

    # print("got reviews")
    product_revs = ["start"]
    for i in reviews:
        try:
            new = i.text
            product_revs.append(new)
        except:
            pass

    catnap()
    # review_type_dropdown.send_keys(Keys.ARROW_DOWN)

    nap()

    return product_revs
    driver.close()


## RUN PROGRAM ------------------------------------------------------------------
if __name__ == "__main__":

    # 1 star
    alls = []

    for i in urls:
        try:
            foo = page_iter(i, 1)
            alls.append(foo)
        except:
            pass

    df1 = pd.DataFrame({"text": alls, "stars": "1"})

    # 2 star
    alls = []

    for i in urls:
        try:
            foo = page_iter(i, 2)
            alls.append(foo)
        except:
            pass

    df2 = pd.DataFrame({"text": alls, "stars": "2"})

    # 3 star
    alls = []

    for i in urls:
        try:
            foo = page_iter(i, 3)
            alls.append(foo)
        except:
            pass

    df3 = pd.DataFrame({"text": alls, "stars": "3"})

    # 4 star
    alls = []

    for i in urls:
        try:
            foo = page_iter(i, 4)
            alls.append(foo)
        except:
            pass

    df4 = pd.DataFrame({"text": alls, "stars": "4"})

    # 5 star
    alls = []

    for i in urls:
        try:
            foo = page_iter(i, 5)
            alls.append(foo)
        except:
            pass

    df5 = pd.DataFrame({"text": alls, "stars": "5"})

    # Combine
    final_df = pd.concat([df1, df2, df3, df4, df5])

    final_df.to_csv("data/full_reviews.csv")

