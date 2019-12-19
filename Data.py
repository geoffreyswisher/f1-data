import http.client
import xml.dom.minidom

class Data:

	def __init__(self, apikey):

		self.apikey = apikey

	def getStage(self, stageid, apikey):

		conn = http.client.HTTPSConnection("api.sportradar.us")
		conn.request("GET", "/formula1/trial/v2/en/sport_events/sr:stage:%d/summary.xml?api_key=%s" % (stageid, apikey))
		res = conn.getresponse()
		data = res.read()

		ugly = data.decode('utf-8')
		xmldata = xml.dom.minidom.parseString(ugly)
		prettyxml = xmldata.toprettyxml()
		
		summary = xmldata.getElementsByTagName('summary')[0]
		stagename = summary.childNodes[0].getAttribute('description')
		stagename = stagename.replace(' ', '_')

		filename = stagename + '.xml'

		f = open('data/stages/%s' % (filename), 'w+')
		f.writelines(prettyxml)

		
		return prettyxml

	def getCompetitor(self, competitorid, apikey):

		conn = http.client.HTTPSConnection("api.sportradar.us")
		conn.request("GET", "/formula1/trial/v2/en/competitors/sr:competitor:%d/profile.xml?api_key=%s" % (competitorid, apikey))
		res = conn.getresponse()
		data = res.read()

		ugly = data.decode('utf-8')
		xmldata = xml.dom.minidom.parseString(ugly)
		prettyxml = xmldata.toprettyxml()

		profile = xmldata.getElementsByTagName('competitor_profile')[0]
		name = profile.childNodes[0].getAttribute('name')
		name = name.replace(' ', '_').replace(',', '')

		filename = name + '.xml'
		f = open('data/competitors/%s' % (filename), 'w+')
		f.writelines(prettyxml)

