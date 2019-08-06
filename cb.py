import nltk
import numpy as np
import random
import string # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#from gtts import gTTS
import eel
import os
import pyttsx3
import wikipediaapi
import sys
sys.path.insert(0, 'C:\\Users\\Debojotee\\Desktop\\ChatBot\\final\\Face-Recognition-master')
import detector as dt

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey","hola")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
uin = ("what", "how", "when", "why","which","where")
vin = ("is")
eel.init('web_app')

def greeting(sentence): 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)



#def LemTokens(tokens):
#    return [lemmer.lemmatize(token) for token in tokens]

#remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

#def LemNormalize(text):
#    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def response(user_response):
    robo_response=''
    
    n=nltk.word_tokenize(user_response)
    i=0
    if (n[0] == 'who' and n[1] == 'am'):
        c=dt.main()
        return c
    elif (n[0] == 'who' and n[1] == 'are'):
        c='about'
        return c
    
    while (i<=len(n)-1):
        if n[i] in uin:
            del n[i]
        elif n[i] in vin:
            del n[i]
        else:
            break
    c = ' '.join(n)
    page_py = wiki_wiki.page(c)


    if(page_py.exists()):
        h=nltk.sent_tokenize(page_py.summary[0:800])
        #print(h)
        hs = ' '.join(h[0:2])
        #print(hs)
        robo_response=robo_response+hs
        return robo_response
    else:
        #robo_response = robo_response+"Sorry there may have been some mistakes"
        return user_response
wiki_wiki = wikipediaapi.Wikipedia('en')

def main():
    #print("DAS: ",end="")
    s="My name is DAS. I will answer your queries. If you want to exit, type Bye!"
    return (s)
@eel.expose
def input(get):
    flag=True
    '''engine.say(s)
    engine.setProperty('rate',180)  
    engine.setProperty('volume',0.9) 
    engine.runAndWait() '''
    while(flag==True):
        user_response = get
        user_response=user_response.lower()
        #print("DAS: ",end="")
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                s=("You are welcome")
                return(s)
                '''engine.say(s)
                engine.runAndWait()'''
            else:
                if(user_response=='change language'):
                    s= "changing..."
                    return(s)
                elif(greeting(user_response)!=None):
                    s=greeting(user_response)
                    return(s)
                else:
                    s=response(user_response)
                    return(s)
                    #sent_tokens.remove(user_response)
        else:
            flag=False
            s="Bye! take care.."
            return (s)
            '''engine.say("Bye! take care")
            engine.runAndWait() '''
            print("")
            print("================================closing======================================")
            print("")

eel.start('index.html', size=(800, 650))
