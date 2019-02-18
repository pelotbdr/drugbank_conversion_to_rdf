#! /usr/bin/env python

import xml.dom.minidom

dataDir = "./"
topic = "full_database.xml"

dataDir = dataDir + topic



def getText(nodelist):
	rc = []
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc.append(node.data)
	return ''.join(rc)


def getID(test):
	result = ""
	datab = xml.dom.minidom.parse(dataDir)
	idList = datab.getElementsByTagName("drugbank-id")
	if test in idList :
		result=test
	return result

print(getID("DB00745"))

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

