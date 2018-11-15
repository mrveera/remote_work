import speech_recognition as sr
import time
from util import speak, recognize_speech_from_mic

class VA():
    def __init__(self, name="potti"):
        self.name = name
        self.guess = None
        self.skills={
        'play music':speak
        }

    def should_listen(self):
        if not self.guess["success"] or self.guess["error"]:
            return False
        if self.guess["transcription"].lower() == self.name.lower():
            return True
        return False

    def add_skill(self, cmd, action):
        if not cmd in self.skills:
            self.skills[cmd]=action
            return
        else:
            raise "Already existed"

    def match_cmd(self, cmd):
        cmds = self.skills.keys()
        possible_cmds = cmd.split(" ")
        for possible_cmd in possible_cmds:
            if possible_cmd in cmds:
                return (True,possible_cmd)
        return (False, None)

    def invoke_cmd(self,cmd,text):
        args =  text.split(" ")
        args.remove(cmd)
        self.skills[cmd](" ".join(args))

    def listen(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        speak("Initialising "+self.name)
        speak("wait")
        while(True):
            print("you can speak")
            self.guess = recognize_speech_from_mic(recognizer, microphone)
            print(self.guess)
            if(self.should_listen()):
                cmd = recognize_speech_from_mic(recognizer, microphone,True)
                if not cmd["success"]:
                    speak("I did not catch that. What did you say?")
                    continue
                if cmd["error"]:
                    speak("I dont know that")
                    continue
                input = cmd["transcription"].lower().replace("'","\\'")
                maybe_cmd = self.match_cmd(input)
                if maybe_cmd[0]:
                    self.invoke_cmd(maybe_cmd[1],input)
                    continue
                speak("unrecognised command "+ input)
            # time.sleep(10)
