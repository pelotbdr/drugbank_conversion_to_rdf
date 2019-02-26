#! /usr/bin/env python

import xml.dom.minidom

dataDir = '../'
#topic = 'full_database'
#topic = 'mini'
topic = 'mini2'

file = dataDir + topic + '.xml'



def getText(nodelist):
	rc = []
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc.append(node.data)
	return ''.join(rc)

prefix = """@prefix : <https://www.irisa.fr/test#> .
@prefix drugbank: <https://www.irisa.fr/test#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> . 
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . 
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfg: <http://www.w3.org/2004/03/trix/rdfg-1/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> . 
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix faldo: <http://biohackathon.org/resource/faldo#> .  
"""

datab = xml.dom.minidom.parse(file)

for drug in datab.getElementsByTagName('drug'):
	if 'type' in drug.attributes :
		name = getText(drug.getElementsByTagName('name')[0].childNodes)			# Drug Name
		output = open('./output/' + name + '.ttl', 'w')
		output.write(prefix + '\n')
		output.write('drugbank:' + name + ' a ' + 'drugbank:drug ;' + '\n')
		
		output.write('\t' + ' drugbank:nameIs "' + name + '"^^xsd:string ;' + '\n')
 		
		output.write('\t' + ' drugbank:idIs "' + getText(drug.getElementsByTagName('drugbank-id')[0].childNodes) + '"^^xsd:string ;' + '\n')			# Drug DrugBank ID
		
		output.write('\t' +  ' drugbank:atcIs "' + drug.getElementsByTagName('atc-code')[0].getAttribute('code') + '"^^xsd:string ;' + '\n') 		# ATC code of the Drug
		
		#listInterDesc = []
		for drugInter in drug.getElementsByTagName('drug-interactions') :
				for drugInter2 in drugInter.getElementsByTagName('drug-interaction') :
					output.write('\t' + ' drugbank:interactsWith "' + getText(drugInter2.getElementsByTagName('drugbank-id')[0].childNodes) + '"^^xsd:string ;' + '\n')		# ID of Drugs interacting with our starting Drug
					#listInterDesc.append(getText(drugInter2.getElementsByTagName('description')[0].childNodes))						# Description of the interactions		
		
		
		for exter_ref in drug.getElementsByTagName('external-identifiers') :
			for exter_ref2 in exter_ref.getElementsByTagName('external-identifier') :
				output.write('\t' + ' drugbank:hasExternalId "' + getText(exter_ref2.getElementsByTagName('resource')[0].childNodes) + ':' + getText(exter_ref2.getElementsByTagName('identifier')[0].childNodes) + '"^^xsd:string ;' + '\n')		# External IDs of the starting Drug
		
		
		for pathway in drug.getElementsByTagName('pathways') :
			for pathway2 in pathway.getElementsByTagName('pathway') :
				for enz in pathway2.getElementsByTagName('enzymes') :
					for i in range(len(enz.getElementsByTagName('uniprot-id'))) :
						output.write('\t' + ' drugbank:interactsWithEnzyme "' + getText(enz.getElementsByTagName('uniprot-id')[i].childNodes) + '"^^xsd:string ;' + '\n')			# Enzymes implicated in the pathway of the starting Drug

		
		for target in drug.getElementsByTagName('targets') :
			for target2 in drug.getElementsByTagName('target') :
				if target2.getAttribute("position") == '1' or 'position' not in target2.attributes:
					output.write('\t' + ' drugbank:drugTargetIs "' + getText(target2.getElementsByTagName('id')[0].childNodes) + ':' + getText(target2.getElementsByTagName('actions')[0].getElementsByTagName('action')[0].childNodes) + '"^^xsd:string ;' + '\n') # Drug Target + action

				for polypep in target2.getElementsByTagName('polypeptide') :
					for exter_ref_target in polypep.getElementsByTagName('external-identifiers') :
						for exter_ref_target2 in exter_ref_target.getElementsByTagName('external-identifier') :
							output.write('\t' + ' drugbank:targetExternalID "' + getText(exter_ref_target2.getElementsByTagName('resource')[0].childNodes) + ':' + getText(exter_ref_target2.getElementsByTagName('identifier')[0].childNodes) + '"^^xsd:string ;' + '\n') # External IDs of the target(s) 
					
					for go in polypep.getElementsByTagName('go-classifiers') :
						for go2 in go.getElementsByTagName('go-classifier') :
							output.write('\t' + ' drugbank:go_' + getText(go2.getElementsByTagName('category')[0].childNodes) + ' "' + getText(go2.getElementsByTagName('description')[0].childNodes) + '"^^xsd:string ;' + '\n')		#GO Classifiers of the  target
		output.write('\t' + ' drugbank:isComplete "TRUE"^^xsd:string .' + '\n')
		print("Progressing ...")
		output.close()
