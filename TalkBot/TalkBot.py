# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:31:46 2021

@author: Prahlad
"""

import speech_recognition as sr
import pyaudio
import pyttsx3
import pyjokes
from datetime import datetime 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



from chatterbot import ChatBot
bot=ChatBot("siri")


from chatterbot.trainers import ChatterBotCorpusTrainer
bot.set_trainer(ChatterBotCorpusTrainer)


bot.train('chatterbot.corpus.english')
listener=sr.Recognizer()


def finder(listWords,search):
    for i in listWords :
        if(i.lower()==search):
            return True
    return False
print(bot.name+"jdbfng")

name=input("Please enter your name ")
talk("hello"+name)
print("Hello My name is Siri")
print("Use the word Siri at the begining to get special replies for current time and a joke ..... ")
print("You can alse get chuck norris jokes by requesting the same to me.....")
print("..........................................................................................\n\n")

print(sr.__version__)
print(sr.Microphone.list_microphone_names())

while (True):
   try:
    with sr.Microphone(device_index=1) as source:
        print(name+":")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        print (command)
        if(command.split(" ")[0].lower()=="siri"):
            if(finder(command.split(" "),"joke")):
                if(finder(command.split(" "),"chuck") or finder(command.split(" "),"norris")):
                    reply=pyjokes.get_joke(category="chuck")
                else:
                    reply=pyjokes.get_joke()
                talk(reply)
                print(bot.name+":"+reply)
            if(finder(command.split(" "),"time")):
                reply ="The current time is "+datetime.now().strftime("%I:%M:%p")
                print(bot.name+":"+reply)
                talk(reply)
        else:
            if(finder(command.split(" "),'bye')):
                reply='  Bye Bye ,Take care!'
                print(bot.name+":"+reply)
                talk(reply)#ending
                break
            else:
                reply=bot.get_response(command)#replies
                talk(reply)
                print(reply)
   except :
    print("say that again")
