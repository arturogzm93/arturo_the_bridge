
from urllib.request import urlopen
from xml.etree.ElementTree import parse

company = 'santander'

newspaper = {'Expansion' : 'https://www.expansion.com/rss/',
             'Economista' : 'https://www.eleconomista.es/rss/',
             'Cinco dias' : 'https://cincodias.elpais.com/estaticos/rss/'}