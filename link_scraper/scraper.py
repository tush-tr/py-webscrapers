import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import urllib.request
import re

url  = "https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&s"
html = urllib.request.urlopen(url)

htmlsoup = BeautifulSoup(html, "lxml")

linktags = htmlsoup.find_all('a',{'class':"points"})

data = []

for link in linktags:
        re = link.get('href')
        data.append(re)


with open('links.csv','w') as F:
  F.write(str(data))
