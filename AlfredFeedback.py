# -*- coding: utf-8 -*-
class AlfredFeedback:
	feedbackDict = {}
	def addItem(self, uniqueIdentifier, argument, title, subtitle = None, icon = None, itemtype = None):
		self.assertUIdentIsNew(uniqueIdentifier)
		self.assertValidItemType(itemtype)
		item = dict( )
		item['arg'] = argument
		if itemtype is not None: item['type'] = itemtype
		elementDict = dict( )
		elementDict['title'] = title
		if subtitle is not None: elementDict['subtitle'] = subtitle
		if icon is not None: elementDict['icon'] = icon
		item['elementDict'] = elementDict
		self.feedbackDict[uniqueIdentifier] = item

	def assertUIdentIsNew(self, uniqueIdentifier):
		if uniqueIdentifier in self.feedbackDict:
			raise NameError(uniqueIdentifier + ' was already added!')

	def assertValidItemType(self, itemtype):
		if itemtype is not None:
			if itemtype != 'file':
				raise Exception('The value of parameter itemtype must be a string containing "file"!')

	def buildFeedbackXML(self):
		xml = '<?xml version="1.0"?>'
		xml += '\n'
		xml += '<items>'
		for (uid, item) in self.feedbackDict.viewitems( ):
			xml += '\n\t'
			xml += '<item uid="' + uid + '"'
			for (attribute, value) in item.viewitems( ):
				# if isinstance(value, str):
				if attribute != 'elementDict':
					xml += ' ' + attribute + '="' + value + '"'
			xml += '>'
			elementDict = item['elementDict']
			for (element, value) in elementDict.viewitems( ):
				xml += '\n\t\t'
				xml += '<' + element + '>' + value + '</' + element + '>'
			xml += '\n\t'
			xml += '</item>'
		xml += '\n'
		xml += '</items>'
		return xml

	def writeFeedback(self):
		print(self.buildFeedbackXML( ))
