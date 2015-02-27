# Python-S60-GPS-Tracker
GPS Tracker and SMS for Symbian S60 using Python Runtimes. 

##Dependencies: Python S60 Runtime. 

On Symbian S60 Platforms you can run python scripts, with the pythonS60 Runtime. 

The script queries the GPS Module on the mobile for

1.Coordinates (Lat, Lang)

2.Heading

3.Speed

4.Course


Return from GPS Module is NEMA Format. 

Sends the String as a SMS to base number, the mobile with the base number is connected to a raspi.

The raspi uses minterm utility to check for messages on the base phone. 
The phone should up as /dev/ttyxxx
Parses messages and plots the lat,lang on google maps. 

Tested using Nokia E71 as the Tracker Mobile. 
Nokia Xpress 5800 was used as base number connected to raspi.
