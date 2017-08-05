try:
  from urllib.request import urlopen
except ImportError:
  from urllib2 import urlopen
from bs4 import BeautifulSoup

foodList = {}

