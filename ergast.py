import requests

URL = 'http://ergast.com/api/f1/2019/results/1.xml'

PARAMS = {'limit': 100}

r = requests.get(url = URL, params = PARAMS)

data = r.content

f = open('ergast.xml', 'w+')

f.writelines(data)

from Ergast import Ergast

e = Ergast()

e.getSeason(2019)