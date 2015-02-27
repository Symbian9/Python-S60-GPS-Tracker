import appuifw
import messaging
import positioning
import location
import e32

positioning.select_module(positioning.default_module())
positioning.set_requestors([{"type":"service",
                             "format":"application",
                             "data":"test_app"}])
							 
mylatitude = 0
mylongitude = 0
speed = 0
heading = 0
def getmyposition():
    result = positioning.position(course=1)
    #print 'all gps data: ', result    
    coordinates=result["position"]
    mylatitude = coordinates["latitude"]
    mylongitude = coordinates["longitude"]
    course = result["course"]
    print course
    speed = course["speed"]
    heading = course["heading"]
    print 'mylatitude: ', mylatitude
    print 'mylongitude:', mylongitude
    print 'speed',speed
    print 'heading ',heading
    return mylatitude, mylongitude, speed, heading

#data = appuifw.query(u"Type your name:", "text")

nbr1 = "03235348241" # change the mobile number here
#nbr2 = "234567" # change the mobile number here
timer = e32.Ao_timer()

while (1): 

    mylatitude = 0
    mylongitude = 0
    print 'getting position'
    mylatitude, mylongitude, speed, heading = getmyposition()
    mylatitude = '%.13f' % mylatitude
    mylongitude = '%.13f' % mylongitude
    speed = '%.13f' % speed
    heading = '%.13f' % heading
    loc = location.gsm_location()
    txt = u"test message  " + mylatitude + u" " + mylongitude + u" " +speed + u" " + heading + u" " + str(loc)


    #if appuifw.query(u"Send message to your 2 friends","query") == True:
       #txt = txt + mylatitude + u" " + mylongitude 
    messaging.sms_send(nbr1, txt)
        #messaging.sms_send(nbr2, txt)
    appuifw.note(u"Messages sent", "info")
    timer.after(60)
    #else:
    #    appuifw.note(u"Well, your Messages are not sent then", "info")
	
	
	
	




