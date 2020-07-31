#first we are importing libraries
#requests library for requesting the web page for data
import requests as req
#Beautifulsoup library for parse the html data
from bs4 import BeautifulSoup
#here we are taking the input username of the instagram account
username = input("enter the username:-")
#here we are taking the input url of the instagram account
geturl = input("enter the url:")
#get the url stuff by the requests library
getreq = req.get(geturl.format(username))
#parse the data using beautifulsoup
getsoup = BeautifulSoup(getreq.text,"html.parser")
cont = getsoup.find("meta",property="og:image")
url = cont.attrs['content']
with open(username+'.jpg',"wb") as pic:
    binary = requests.get(url).content
    pic.write(binary)

