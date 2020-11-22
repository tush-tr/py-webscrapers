import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import urllib.request
import re

url = "https://www.firstpost.com/firstcricket/sports-news/dc-vs-kxip-live-score-ipl-2020-today-cricket-match-between-delhi-capitals-kings-xi-punjab-online-at-dubai-8832031.html"
def score():
    geturl = requests.get(url)
    soup = BeautifulSoup(geturl.content,'html.parser')
    table = soup.find_all('table')[0]
    score = pd.read_html(str(table))
    print(score)



