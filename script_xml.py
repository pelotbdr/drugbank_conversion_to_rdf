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
		print(name)																# Drug Name
		id= getText(drug.getElementsByTagName('drugbank-id')[0].childNodes)
		print(id)																# Drug Drugbank ID
		atcCode=drug.getElementsByTagName('atc-code')[0].getAttribute('code')
		print(atcCode)															# Drug ATC code
		listInterID = []
		listInterDesc = []
		for drugInter in drug.getElementsByTagName('drug-interactions') :
				for drugInter2 in drugInter.getElementsByTagName('drug-interaction') :
					listInterID.append(getText(drugInter2.getElementsByTagName('drugbank-id')[0].childNodes))						# ID of Drugs interacting with our starting Drug
					listInterDesc.append(getText(drugInter2.getElementsByTagName('description')[0].childNodes))						# Description of the interactions
		externalList = {}
		for exter_ref in drug.getElementsByTagName('external-identifiers') :
			for exter_ref2 in exter_ref.getElementsByTagName('external-identifier') :
				externalList[getText(exter_ref2.getElementsByTagName('resource')[0].childNodes)] = getText(exter_ref2.getElementsByTagName('identifier')[0].childNodes)		# External IDs of the starting Drug
		enzymes = []
		for pathway in drug.getElementsByTagName('pathways') :
			for pathway2 in pathway.getElementsByTagName('pathway') :
				for enz in pathway2.getElementsByTagName('enzymes') :
					for i in range(len(enz.getElementsByTagName('uniprot-id'))) :
						enzymes.append(getText(enz.getElementsByTagName('uniprot-id')[i].childNodes))					# Enzymes implicated in the pathway of the starting Drug
		drugTarget = {}
		externalListTarget = {}
		goClassif = {}
		for target in drug.getElementsByTagName('targets') :
			for target2 in drug.getElementsByTagName('target') :
				drugTarget[getText(target2.getElementsByTagName('id')[0].childNodes)] = getText(target2.getElementsByTagName('actions')[0].getElementsByTagName('action')[0].childNodes)  # Drug Target
				for polypep in target2.getElementsByTagName('polypeptide') :
					for exter_ref_target in polypep.getElementsByTagName('external-identifiers') :
						for exter_ref_target2 in exter_ref_target.getElementsByTagName('external-identifier') :
							externalListTarget[getText(exter_ref_target2.getElementsByTagName('resource')[0].childNodes)] = getText(exter_ref_target2.getElementsByTagName('identifier')[0].childNodes) # External IDs of the target
					for go in polypep.getElementsByTagName('go-classifiers') :
						for go2 in go.getElementsByTagName('go-classifier') :
							if getText(go2.getElementsByTagName('category')[0].childNodes) in goClassif :																		# GO classifiers of the target
								goClassif[getText(go2.getElementsByTagName('category')[0].childNodes)] += "," + getText(go2.getElementsByTagName('description')[0].childNodes)
							else :
								goClassif[getText(go2.getElementsByTagName('category')[0].childNodes)] = getText(go2.getElementsByTagName('description')[0].childNodes)
		
			