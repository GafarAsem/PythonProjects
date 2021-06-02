import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json

def getElementText(name, dict, soup):
        elements = soup.find(name, dict)
        print(elements.text)
        return elements.text

def getElement(name, dict, soup):
        elements = soup.find(name, dict)
        return elements

def getElementContent(name, dict, key, soup):
        elements = soup.find(name, dict)
        print(elements[key])
        return elements[key]


playlist_url=requests.get('https://grey.egybest.network/explore/?q=happy')
soup = BeautifulSoup(playlist_url.content, "html.parser")

dateMovie = getElement('div', {'class': 'movie_title tam'}, soup)
dateMovie = getElementText('a', {},dateMovie)

print(dateMovie)
