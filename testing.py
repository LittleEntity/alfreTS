# -*- coding: UTF-8 -*-
from AlfredFeedback import AlfredFeedback

feedback = AlfredFeedback( )
feedback.addItem( 1, 'FRST', 'first', 'First Item', '/path/anIcon.png')
feedback.addItem( 2, 'SCND', 'second', 'Second Item', '/anotherPath/myIcon.png', 'file' )
feedback.writeFeedback( )
