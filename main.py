
import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
import threading


print("-" * 60)
print(" Project: Voice based Email for blind")
print(" <--Created by Pigeon-->")
print("-" * 60)


# project name
tts = gTTS(text="Project: Voice based Email for blind", lang='en')
ttsname = ("path/name.mp3")
tts.save(ttsname)

music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)

# login from os
login = os.getlogin
print("You are logging from : " + login())

def setInterval(func,time, str):
        e = threading.Event()
        while not e.wait(time):
            func(str)
            break

def foo(str):
        print(str)

def repeat():
        
    # choices
    print("1. Composed a mail.")
    tts = gTTS(text="option 1. Composed a mail.", lang='en')
    ttsname = ("path/hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    print("2. Save note to drive")
    tts = gTTS(text="option 2. Save note to drive", lang='en')
    ttsname = ("hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    print("3. Create Events on Google Calenders")
    tts = gTTS(text="option 3. Create Events on Google Calenders", lang='en')
    ttsname = ("hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    # this is for input choices
    tts = gTTS(text="Your choice : ", lang='en')
    ttsname = ("path/hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    #Automated email composing part

    


    # voice recognition part
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")

    setInterval(foo,8, "You have chosen option 1 - Composed a mail")


    tts = gTTS(text="You have chosen option 1 - Composed a mail", lang='en')
    ttsname = ("path/hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    setInterval(foo,5,"")

    tts = gTTS(text="listening for email I D", lang='en')
    ttsname = ("path/hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)


    setInterval(foo,6, "Composing email from pigeonisyourdad@gmail.com")

    tts = gTTS(text="Listening for your message", lang='en')
    ttsname = ("path/hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    setInterval(foo,7, "Sending email....")
    
    tts = gTTS(text="Sending email", lang='en')
    ttsname = ("path/hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    setInterval(foo,8, "Email Sent Successfully")

    
    tts = gTTS(text="Email Sent Successfully", lang='en')
    ttsname = ("path/hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

repeat()
setInterval(foo,5, "")
repeat()



audio = r.listen(source)
print("ok done!!")
try:
 text = r.recognize_google(audio)
 print("You said : " + text)
except sr.UnknownValueError:
 print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
 print("Could not request results from Google Speech Recognition service;{0}".format(e))

# choices details
if int(text) == 1:
 r = sr.Recognizer() # recognize
 with sr.Microphone() as source:
     print("Your message :")
     audio = r.listen(source)
     print("ok done!!")
 try:
     text1 = r.recognize_google(audio)
     print("You said : " + text1)
     msg = text1
 except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio.")
 except sr.RequestError as e:
     print("Could not request results from Google Speech Recognition service;{0}".format(e))
        
 mail = smtplib.SMTP('smtp.gmail.com', 587) # host and port area
 mail.ehlo() # Hostname to send for this command defaults to the FQDN of the localhost.
 mail.starttls() # security connection
 mail.login('emailID', 'pswrd') # login part
 mail.sendmail('emailID', 'victimID', msg) # send part
 print("Congrates! Your mail has send. ")
 tts = gTTS(text="Congrates! Your mail has send. ", lang='en')
 ttsname = ("path/send.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)
 mail.close()
    
if int(text) == 2:
 mail = imaplib.IMAP4_SSL('imap.gmail.com', 993) # this is host and port area.... sslsecurity
 unm = ('your mail/ victim mail') # username
 psw = ('pswrd') # password
 mail.login(unm, psw) # login
 stat, total = mail.select('Inbox') # total number of mails in inbox
 print("Number of mails in your inbox :" + str(total))
 tts = gTTS(text="Total mails are :" + str(total), lang='en') # voice out
 ttsname = ("path/total.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)

 # unseen mails
 unseen = mail.search(None, 'UnSeen') # unseen count
 print("Number of UnSeen mails :" + str(unseen))
 tts = gTTS(text="Your Unseen mail :" + str(unseen), lang='en')
 ttsname = ("path/unseen.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)
    
 # search mails
 result, data = mail.uid('search', None, "ALL")
 inbox_item_list = data[0].split()
 new = inbox_item_list[-1]
 old = inbox_item_list[0]
 result2, email_data = mail.uid('fetch', new, '(RFC822)') # fetch
 raw_email = email_data[0][1].decode("utf-8") # decode
 email_message = email.message_from_string(raw_email)
 print("From: " + email_message['From'])
 print("Subject: " + str(email_message['Subject']))
 tts = gTTS(text="From: " + email_message['From'] + " And Your subject: " + str(email_message['Subject']), lang='en')
 ttsname = ("path/mail.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)

 # Body part of mails
 stat, total1 = mail.select('Inbox')
 stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
 msg = data1[0][1]
 soup = BeautifulSoup(msg, "html.parser")
 txt = soup.get_text()
 print("Body :" + txt)
 tts = gTTS(text="Body: " + txt, lang='en')
 ttsname = ("path/body.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)
 mail.close()
 mail.logout()
