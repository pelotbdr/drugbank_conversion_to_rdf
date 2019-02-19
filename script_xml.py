#! /usr/bin/env python

import xml.dom.minidom

dataDir = '../'
#topic = 'full_database'
topic = 'mini'

file = dataDir + topic + '.xml'



def getText(nodelist):
	rc = []
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc.append(node.data)
	return ''.join(rc)

result = ""
datab = xml.dom.minidom.parse(file)
drugList = datab.getElementsByTagName('drug')

for drug in drugList:
	if 'type' in drug.attributes :
		name = getText(drug.getElementsByTagName('name')[0].childNodes)
		print(name)
		id= getText(drug.getElementsByTagName('drugbank-id')[0].childNodes)
		print(id)
		atcCode=drug.getElementsByTagName('atc-code')[0].getAttribute('code')
		print(atcCode)
		
		drugInteractionsList = drug.getElementsByTagName('drug-interactions')
		for drug in drugInteractionsList :
				drug_2 = drug.getElementsByTagName('drug-interaction')
				test = getText(drug_2.getElementsByTagName('drugbank-id'))
				print(text)
			
		

