from flask import Flask, Markup, jsonify, request
from selectorlib import Extractor
import requests

app = Flask(__name__)

distance_yml = """
distance:
    css: 'div[class="BbbuR uc9Qxb uE1RRc"]'
    xpath: null
    multiple: false
    type: Text
"""

e = Extractor.from_yaml_string(distance_yml)

@app.route('/', methods=['GET'])
def home():
    return "<h1>TravelGuide-Backend</h1><p>URL: <a href='/api/v1/distance?city_1=Karachi&city_2=Sialkot'>Distance (modify city_1 and city_2 in the URL to change cities)</a></p>"


@app.route('/api/v1/distance', methods=['GET'])
def api_all():
    city_1 = request.args.get('city_1')
    city_2 = request.args.get('city_2')

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.google.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    if not city_1 or not city_2:
        return "Please enter 2 cites so we can calculate the distance betweeen the two."
    URL = "https://www.google.com/search?sxsrf=ALeKk022Hiy2uX5Gm1ilznFTe2MIB6Hyxw%3A1607181814645&ei=9qXLX8n6JpSFhbIPstab-A8&q=" + city_1 +"+to+" + city_2 + "+distance&oq=karachi+to+lahore+distance&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABg0uAlaABwAngAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjJzZrpkrftAhWUQkEAHTLrBv8Q4dUDCA0&uact=5"

    # URL = "https://www.google.com/search?sxsrf=ALeKk022Hiy2uX5Gm1ilznFTe2MIB6Hyxw%3A1607181814645&ei=9qXLX8n6JpSFhbIPstab-A8&q=karachi+to+sialkot+distance&oq=karachi+to+lahore+distance&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABg0uAlaABwAngAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjJzZrpkrftAhWUQkEAHTLrBv8Q4dUDCA0&uact=5"

    r = requests.get(URL, headers=headers)
    if r.status_code > 500:
        return {}
    return jsonify(e.extract(r.text))
