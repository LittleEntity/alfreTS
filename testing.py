# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from AlfredFeedback import AlfredFeedback

feedback = AlfredFeedback( )
feedback.addItem( 1, u'FRST', u'first', u'First Item', u'/path/anIcon.png')
feedback.addItem( 2, u'SCND', u'second', u'Second Item', u'/anotherPath/myIcon.png', u'file' )
feedback.addItem( 3, u'THRD', u'ßpêcîâl', u'', u'/wherever/superIcon.png', u'file' )
feedback.writeFeedback( )

myLocale = ('el_GR', 'UTF-8')
#myLocale = ('de_DE', 'UTF-8')
formatList = [
	("%Y%m%d%H%M", "YearMonthDayHourMinute for versioning"),
	("%x %X", "Date and time representation appropriate to locale setting"),
	#("%A %d.%b.%Y um %H:%M Uhr", "German date representation"),
	("%A, %B %d, %Y at %Hh:%M %p", "US date representation"),
]

execfile("main.py")
main(formatList)
