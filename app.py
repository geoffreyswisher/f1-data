import http.client
import xml.dom.minidom

key = ''

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/formula1/trial/v2/en/sport_events/sr:stage:426678/summary.xml?api_key=%s" % (key))

res = conn.getresponse()
data = res.read()

ugly = data.decode('utf-8')

xml = xml.dom.minidom.parseString(ugly)

prettyxml = xml.toprettyxml()

f = open('data.xml', 'w')

f.writelines(prettyxml)

print(prettyxml)
