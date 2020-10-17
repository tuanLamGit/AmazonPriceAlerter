import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import json
import ssl

ctx = ssl.create_default_context()

url = "https://www.amazon.com/gp/product/B085M7NVGR?pf_rd_r=0931C8TT1XN1DWHZZWVG&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
product_json = {}

for divs in soup.find_all('div'):
  try:
    price = str(divs['data-asin-price'])
    product_json['price'] = '$' +price
    break
  except:
    pass