#!/usr/bin/python3

import xml.dom.minidom

filename = "abudhabi2019.xml"

doc = xml.dom.minidom.parse(filename)


for team in doc.getElementsByTagName('team'):

	points = team.childNodes[1].getAttribute('points')

	if not points:
		points = "0"

	print("\t%s. %s : %s points " % (team.childNodes[1].getAttribute('position'), team.getAttribute('name'), points))


