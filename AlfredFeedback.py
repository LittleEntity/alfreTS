# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET

class AlfredFeedback:
	itemsElement = ET.Element( 'items' )

	def addItem( self, 
	uniqueIdentifier, 
	argument, 
	title, 
	subtitle = None, 
	icon = None, 
	itemtype = None ):
		uniqueIdentifier = str( uniqueIdentifier )
		self.assertUIdenIsNew( uniqueIdentifier )
		self.assertValidItemType( itemtype )
		itemElement = ET.SubElement( self.itemsElement, 'item' )
		itemElement.set( 'uid', uniqueIdentifier )
		itemElement.set( 'arg', argument )
		if itemtype is not None: itemElement.set( 'type', itemtype )
		titleElement = ET.SubElement( itemElement, 'title' )
		titleElement.text = title
		if subtitle is not None:
			subtitleElement = ET.SubElement( itemElement, 'subtitle' )
			subtitleElement.text = subtitle
		if icon is not None:
			iconElement = ET.SubElement( itemElement, 'icon' )
			iconElement.text = icon

	def assertUIdenIsNew( self, uniqueIdentifier ):
		for child in self.itemsElement:
			if uniqueIdentifier == child.get( 'uid' ):
				errorString = 'the identifier \"' + uniqueIdentifier + '\" was already added!'
				raise NameError(errorString)

	def assertValidItemType( self, itemtype ):
		if itemtype is not None:
			if itemtype != 'file':
				raise Exception('The value of parameter itemtype must be a string containing "file"!')

	def writeFeedback( self ):
		response = ET.tostring( self.itemsElement, 'UTF-8', 'xml' )
		print( response )
