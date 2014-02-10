# alfreTS #

This is a time stamp workflow for the [Alfred Application](http://www.alfredapp.com/).

Open the alfred window then type `now`. The results show the current timestamp in different formats. Selecting an option will result in the shown formatted timestamp being copied to the clipboard.

You can define your own formats via the python [strftime](http://strftime.org/) syntax. It is also possible to define your preferred locale setting to acquire the weekday and month names in your local language. In order to edit these settings you need to enter the settings into the script of the Script Filter inside the workflow. This can be done by editing the `#commented` lines. (In case you did not know how `#comments` work: lines with `#` in front will be ignored by the python interpreter and not be executed.)
