import requests

class Ergast:

    def getSeason(self, year):
        
        URL = 'http://ergast.com/api/f1/' + str(year) + '.xml'
        PARAMS = {'limit': 100}

        res = requests.get(url = URL, params = PARAMS)
        data = res.content
        
        f = open('edata/seasons/' + str(year) + '.xml', 'w+')
        f.writelines(data)

        return data