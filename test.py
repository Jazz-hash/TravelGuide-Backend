from selectorlib import Extractor
import requests 
import json 
from time import sleep
from flask import Flask

print("Test Passed ! All libraries working.")


yml_string = """
products:
    css: 'div[data-component-type="s-search-result"]'
    xpath: null
    multiple: true
    type: Text
    children:
        title:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Text
        url:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Link
        rating:
            css: 'div.a-row.a-size-small span:nth-of-type(1)'
            xpath: null
            type: Attribute
            attribute: aria-label
        reviews:
            css: 'div.a-row.a-size-small span:nth-of-type(2)'
            xpath: null
            type: Attribute
            attribute: aria-label
        price:
            css: 'span.a-price:nth-of-type(1) span.a-offscreen'
            xpath: null
            type: Text
"""

e = Extractor.from_yaml_string(yml_string)

def scrape(url):  
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    r = requests.get(url, headers=headers)
    if r.status_code > 500:
        return {}
    return e.extract(r.text)
url_amazon = "https://www.amazon.com/s?k=RTX+3090"
print(scrape(url_amazon))