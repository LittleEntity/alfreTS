# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from AlfredFeedback import AlfredFeedback

feedback = AlfredFeedback( )
feedback.addItem( 1, u'FRST', u'first', u'First Item', u'/path/anIcon.png')
feedback.addItem( 2, u'SCND', u'second', u'Second Item', u'/anotherPath/myIcon.png', u'file' )
feedback.addItem( 3, u'THRD', u'ßpêcîâl', u'', u'/wherever/superIcon.png', u'file' )
feedback.writeFeedback( )
