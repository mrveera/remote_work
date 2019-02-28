from va import VA
from util import speak
import os,sys


pathname = os.path.dirname(sys.argv[0])
abs_dir = os.path.abspath(pathname)

def start_zoom_meeting(cmd):
    speak("starting zoom meeting for remote work")
    zoom_name = os.getenv("ZOOM_NAME", "None")
    zoom_id = os.getenv("ZOOM_ID","0")
    os.popen(abs_dir +"/zoom.sh --name="+zoom_name+" "+zoom_id)

def play_music(cmd):
    speak("I will play wait")
    os.popen("cd ~/Downloads/songs && vlc .")

def open_jenkins(cmd):
    speak("opening jenkins radiator view")
    jenkins = os.getenv("JENKINS_URL","http://google.com")
    os.popen("open "+ jenkins)

def updating_me(cmd):
    speak("updating myself wait")
    os.popen("cd "+ abs_dir + " && git pull")
    sys.exit(242)

va = VA("alexa")
va.add_skill("zoom",start_zoom_meeting)
va.add_skill("open_jenkins",open_jenkins)
va.add_skill("play",play_music)
va.add_skill("self_update", updating_me)
va.listen()
