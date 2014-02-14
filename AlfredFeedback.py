# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import xml.etree.ElementTree as ET

class AlfredFeedback:
	#itemsElement = ET.Element( u'items' )

	def __init__(self):
		self.itemsElement = ET.Element( u'items' )

	def addItem(	
			self, 
			uniqueIdentifier, 
			argument, 
			title,
			subtitle = None, 
			icon = None, 
			itemtype = None ):
		uniqueIdentifier = str( uniqueIdentifier )
		self.assertUIdenIsNew( uniqueIdentifier )
		self.assertValidItemType( itemtype )
		itemElement = ET.SubElement( self.itemsElement, u'item' )
		itemElement.set( u'uid', uniqueIdentifier )
		itemElement.set( u'arg', argument )
		if itemtype is not None: itemElement.set( u'type', itemtype )
		titleElement = ET.SubElement( itemElement, u'title' )
		titleElement.text = title
		if subtitle is not None:
			subtitleElement = ET.SubElement( itemElement, u'subtitle' )
			subtitleElement.text = subtitle
		if icon is not None:
			iconElement = ET.SubElement( itemElement, u'icon' )
			iconElement.text = icon

	def assertUIdenIsNew( self, uniqueIdentifier ):
		for child in self.itemsElement:
			if uniqueIdentifier == child.get( u'uid' ):
				errorString = ( u'the identifier \"' + uniqueIdentifier 
					+ u'\" was already added!' )
				raise NameError( errorString )

	def assertValidItemType( self, itemtype ):
		if itemtype is not None:
			if itemtype != u'file':
				raise Exception( u'The value of parameter itemtype' 
					u'must be a string containing "file"!' )

	def writeFeedback( self ):
		response = ET.tostring( self.itemsElement )
		print( response.encode( 'UTF-8' ) )
