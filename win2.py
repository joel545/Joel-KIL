import requests
from bs4 import BeautifulSoup
html_data1 = requests.get("http://tw.yahoo.com")
html_data2 = requests.get("https://www.su101.net/")
soup1=BeautifulSoup(html_data1.text,"html.parser")
soup2=BeautifulSoup(html_data2.text,"html.parser")
webtitle1=soup1.title
webtitle2=soup2.title
print ("http://tw.yahoo.com","(web title 1:)",webtitle1)
print ("https://www.su101.net/","(web title 2:)",webtitle2)
