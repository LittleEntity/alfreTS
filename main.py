# -*- coding: utf-8 -*-
from AlfredFeedback import AlfredFeedback
from locale import setlocale, LC_ALL
from time import localtime, strftime, time

def main(formatList):
	setlocale(LC_ALL, myLocale) # affects strftime
	feedback = AlfredFeedback( )
	counter = 0
	for (format, description) in formatList:
		counter += 1
		nowLocalizedTimestamp = localtime(time( ))
		formattedTimestamp = (strftime(format, nowLocalizedTimestamp)).decode('utf-8')
		feedback.addItem(
			str(counter), 
			formattedTimestamp, 
			formattedTimestamp, 
			description, 'icon.png'
		)
	feedback.writeFeedback( )
