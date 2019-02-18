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



for i in range(drugList):
	name = drugList[i].getElementsByTagName('name')
	idList_unfiltered = drugList[i].getElementsByTagName('drugbank-id')
	idList= []
	for i in range(idList_unfiltered) :
		if idList_unfiltered[i].getAttribute('primary') == 'true' :
			idList.append.idList_unfiltered[i]
	atcCode = drugList[i].getElementsByTagName('atc-code').getAttribute('code')
	drugInteractions_tofilter = drugList[i].getElementsByTagName('drug-interactions')
	drugInteractions = drugInteractions_tofilter.getElementsByTagName('drugbank-id')
	
print(name)
print(idList)
print(atcCode)
	

def getCitationList(pmid):
	citations = []
	domArticle = xml.dom.minidom.parse(dataDir + pmid + ".xml")
	citationElts = domArticle.getElementsByTagName('CommentsCorrections')
	for currentCitation in citationElts:
		if currentCitation.getAttribute('RefType') != "Cites":
			continue
		for currentCitationRef in currentCitation.getElementsByTagName('PMID'):
			print(getText(currentCitationRef.childNodes))
			citations.append(getText(currentCitationRef.childNodes))
	return citations

#getCitationList('23110428')
