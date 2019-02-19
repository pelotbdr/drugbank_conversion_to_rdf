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


datab = xml.dom.minidom.parse(file)

for drug in datab.getElementsByTagName('drug'):
	if 'type' in drug.attributes :
		name = getText(drug.getElementsByTagName('name')[0].childNodes)
		print(name)
		id= getText(drug.getElementsByTagName('drugbank-id')[0].childNodes)
		print(id)
		atcCode=drug.getElementsByTagName('atc-code')[0].getAttribute('code')
		print(atcCode)
		listInterID = []
		listInterDesc = []
		for drugInter in drug.getElementsByTagName('drug-interactions') :
				for inter in drugInter.getElementsByTagName('drug-interaction') :
					listInterID.append(getText(inter.getElementsByTagName('drugbank-id')[0].childNodes))
					listInterDesc.append(getText(inter.getElementsByTagName('description')[0].childNodes))
		externalList = {}
		for exter_ref in drug.getElementsByTagName('external-identifiers') :
			for exter_ref2 in exter_ref.getElementsByTagName('external-identifier') :
				externalList[getText(exter_ref2.getElementsByTagName('resource')[0].childNodes)] = getText(exter_ref2.getElementsByTagName('identifier')[0].childNodes)
		print(externalList)
					
		
		
		

