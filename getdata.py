#!/usr/bin/python3

import http.client
import xml.dom.minidom

key = 's67wt459muuhe5c9mus424v3'

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/formula1/trial/v2/en/sport_events/sr:stage:432275/summary.xml?api_key=%s" % (key))

res = conn.getresponse()
data = res.read()

ugly = data.decode('utf-8')

xml = xml.dom.minidom.parseString(ugly)

prettyxml = xml.toprettyxml()

f = open('abudhabi2019.xml', 'w')

f.writelines(prettyxml)

print(prettyxml)
