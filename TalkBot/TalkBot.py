# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:31:46 2021

@author: Prahlad
"""
#importing all the requirements 
import speech_recognition as sr
import pyaudio
import pyttsx3
import pyjokes
from datetime import datetime 



#setting up the talk function to give audio replies 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
###################################################


#Initial chat bot setup and its training 
from chatterbot import ChatBot
bot=ChatBot("siri")


from chatterbot.trainers import ChatterBotCorpusTrainer
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train('chatterbot.corpus.english')




####################################################
listener=sr.Recognizer()             #Listener for a user input 


def finder(listWords,search):        # boolean function to return if a search word is present a array of strings
    for i in listWords :
        if(i.lower()==search):
            return True
    return False
print(bot.name)


name=input("Please enter your name ") # users name 
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
        
        voice=listener.listen(source) #making the listener listen to the microphone input 
        command=listener.recognize_google(voice)#audio to text conversion using google recognizer
        print(name+":"+command)
        if(command.split(" ")[0].lower()=="siri"):  #if a special request such as time or joke is made 
            if(finder(command.split(" "),"joke")):
                if(finder(command.split(" "),"chuck") or finder(command.split(" "),"norris")):
                    reply=pyjokes.get_joke(category="chuck")
                else:
                    reply=pyjokes.get_joke()#getting text responses from the chatterbot 
                talk(reply)#giving the same response in the audio form 
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
    talk("say that again")
    #if the audio was not clear or some other exception occurs 
