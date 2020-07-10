from django.shortcuts import render

# Create your views here.

import requests
from bs4 import BeautifulSoup as bs

#getting news from times of india
toi_url = "https://timesofindia.indiatimes.com/india/coronavirus-pandemic-live-updates-india-covid-cases-deaths-10-july-2020/liveblog/76883922.cms"
toi_r = requests.get(toi_url)
toi_soup = bs(toi_r.content, 'html5lib')
#print(toi_soup.prettify())
toi_content = toi_soup.find_all('div', class_ = "_1KydD")
toi_news=[]
for toi_topic in toi_content:
    toi_news.append(toi_topic.text)
   # print(toi_head.text)
   # print()

#getting news from hindustan times
ht_url = "https://liveupdates.hindustantimes.com/india/coronavirus-india-world-latest-news-covid-19-death-toll-july-8-2020-21594171380795.html"
ht_r = requests.get(ht_url)
ht_soup = bs(ht_r.content, 'html5lib')
#print(ht_soup.prettify())
ht_content = ht_soup.find_all('div', class_ = "article")
#print(ht_content.prettify)
ht_news=[]
for ht_topic in ht_content:
    ht_news.append(ht_topic.text)
    #print(body.text)
    #print()


def index(req):
    return render(req,'COVID/index.html',{"toi_news":toi_news, "ht_news":ht_news})