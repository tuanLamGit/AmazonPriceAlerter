import requests
import urllib.request
import urllib.parse
import urllib.error
import ssl
import json
import time
import lxml
from bs4 import BeautifulSoup 

class Product:
  def __init__(self, url):
    self.url = url
    self.response = requests.get(self.url)
    self.soup = BeautifulSoup(self.response.content, "xml")
  
  def productName(self):
    name = self.soup.find_all("span", {"class": "glow"})
    if str(name) != "None":
      name = str(name)
      for i in name.split():
       print(i)
    else:
      print(str(name))
    #return ret

  def test(self):
    soup = BeautifulSoup(self.response.content, "xml")
    ret = soup.find("productTitle").string
    return ret

url = "https://www.amazon.com/Xbox-One-1TB-Console-Previous-Generation/dp/B089M5L82M/ref=sr_1_1?dchild=1&keywords=xbox&qid=1602964331&sr=8-1"



item = Product(url)
item.__init__(url)
#ret = str(item.productName())
#print(ret)
item.productName()
test = item.test()
print(test)