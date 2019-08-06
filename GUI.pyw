from tkinter import *
import cb as c1
import speech_recognition as sr
import os
import pyttsx3
import time
import threading
from googlesearch import search
import webbrowser
import link
voices_en = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
voices_hin='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_KalpanaM'


voice_get='h'
window = Tk()
engine = pyttsx3.init()
engine.setProperty('rate',180)
engine.setProperty('voice', voices_en)
engine.setProperty('volume',0.9) 
messages = Text(window)
messages.pack()
hyperlink = link.HyperlinkManager(messages)
h=''


def aud(a):
    try:
        
        engine.say(a)
        engine.runAndWait()

        engine.setProperty('voice', voices_en)
    except:
        print ("Can not start speaker or different language")

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)
p=c1.main()

def op(p):
    messages.insert(INSERT, 'DAS: ' + p + '\n')
    aud(p)
    return
    
def callback(h):
    webbrowser.open_new(h)
    

def prin(s):
    try:
        messages.insert(INSERT, '\nDAS: ' + s +'\n')
    except:
        print("cannot insert please restart")

def recog():
    global voice_get
    r = sr.Recognizer()
    aud = sr.Microphone(device_index=1)

    with aud as source:
        
        audio = r.listen(source)

    keyw='ZSAYTXFHZKFMAR4JG3JIVQGGWVIGQAS2'
    text=r.recognize_wit(audio,keyw)
    voice_get=text
    print(voice_get)
    Enter_pressed(True)

def Enter_pressed(event):
    global voice_get
    print(voice_get)
    voice_g=voice_get
    if (voice_g == 'h'):
        input_get = input_field.get()
    else:
        input_get=voice_g
    #print(input_get)
    
    messages.insert(INSERT, '\n>>> %s\n' % input_get)
    
    sp=c1.input(input_get)
    sa=sp
    j=''
    
    if (sp==input_get):
        for j in search(sp, tld="co.in", num=1, stop=1, pause=2):
            sa='check these links\n\n'
            sp=sa
            h=j
            j='i'
            
    elif (sp=="Bye! take care.."):
        #t1.join()
        window.destroy()
        exit()
    elif (sp=="changing..."):
        engine.setProperty('voice', voices_hin)
        sp=sa='मेरा नाम दास है। मैं आपके प्रश्नों का जवाब देंगे। यदि आप समाप्त करना चाहते हैं, तो "BYE" टाइप करें! मैं निर्माण के तहत कर रहा हूँ। मैं जल्द ही उपलब्ध हो जाएगा। भाषा अंग्रेजी में अपडेट हो रही है'
    t1 = threading.Thread(target=prin, args=(sp,))
    t2 = threading.Thread(target=aud, args=(sa,))
    t1.start()
    input_user.set('')
    t2.start()
    if j=='i':
        button = Button(frame_main , text=input_get, width=25, command=lambda aurl=h:callback(aurl)) 
        button.pack()
        #messages.insert(INSERT, '\t' +h, hyperlink.add(h))
    input_get=''
    voice_get='h'
    return "break"
def main():
    
    t3 = threading.Thread(target=op, args=(p,))
    t3.start()
    input_field.bind('<Return>', Enter_pressed)

    frame_main.pack()

    window.mainloop()
frame_main = Frame(window)  # , width=300, height=300)
button = Button(frame_main , text='Mic', width=25, command=lambda: recog())
button.pack()

main()
