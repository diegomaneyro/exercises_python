import pip
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('http://es.wikipedia.org/wiki.Python')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
