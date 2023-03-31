import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from jamdict import Jamdict
from pygoogletranslation import Translator
from langdetect import detect
import speech_recognition as sr 
from gtts import gTTS
from pygame import mixer
from io import BytesIO
import os
import time
root = tk.Tk()
root.title("Japanese Dictionary")
root.geometry("555x555")
style = ttk.Style(root)
root.resizable(width=FALSE, height=FALSE)
'''root.tk.call('source', 'Azure-ttk-theme-main/azure/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground='white')
style.configure("Togglebutton", foreground='white')

button = ttk.Button(
	root,
	text="Here I am - Accent",
	style="Accentbutton")
button.pack()
 
var = tk.StringVar()
togglebutton = ttk.Checkbutton(
	root,
	text='Toggle button',
	style='Togglebutton',
	variable=var,
	onvalue=1)
 
togglebutton.pack()
var2 = tk.StringVar()
togglebutton2 = ttk.Checkbutton(
	root,
	text='Switch button',
	variable=var2,
	onvalue=1,
	style="Switch")
togglebutton2.pack()
'''
def lang_detect(patterns):
    #global lang_detector
    lang_detector = detect(patterns)
    print("Translate from "+lang_detector)
    return lang_detector
def translate_to_ja(patterns):
    global lang_src
    lang_src = lang_detect(patterns)
    try:
        translator = Translator()
        translation = translator.translate(patterns,src = '%s'%lang_src,dest = 'ja')
        #preprocess to remove unnecessary result of pygoogletranslation 
        # initializing substrings
        sub1 = "text="
        sub2 = ", pronunciation"
        # getting index of substrings
        idx1 = str(translation).index(sub1)
        idx2 = str(translation).index(sub2)
        result_ja = ''
        # getting elements in between
        for idx in range(idx1 + len(sub1) , idx2):
            result_ja = result_ja + str(translation)[idx]
        print('Translation results: '+result_ja)
        return result_ja
    except StopIteration:
        pass
def translate_to_dest(patterns):
    try:
        translator_dest = Translator()
        translation = translator_dest.translate(patterns,src = 'en',dest = '%s'%lang_src)
        #preprocess to remove unnecessary result of pygoogletranslation 
        # initializing substrings
        sub3 = "text="
        sub4 = ", pronunciation"
        # getting index of substrings
        idx3 = str(translation).index(sub3)
        idx4 = str(translation).index(sub4)
        result_dest = ''
        # getting elements in between
        for idx in range(idx3 + len(sub3) , idx4):
            result_dest = result_dest + str(translation)[idx]
        print("Translate result: "+result_dest)
        return result_dest
    except StopIteration:
        pass
def word_lookup(patterns):
	jam = Jamdict()
	translate = translate_to_ja(patterns)
	results = jam.lookup(translate)
	return str(results)
def if_kanji(patterns):
    jam = Jamdict()
    results = jam.lookup(patterns)
    return str(results)
def open_drawing_strokes():
    os.system('start KanjiStrokes/KanjiStrokes.exe')
def open_handwriting():
    os.system('python handwritten.py')
def search_entry():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    lang_source = detect(msg)
    if msg!='':
        Dictionary.config(state=NORMAL)
        Dictionary.insert(END, "You: "+ msg + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        res =  word_lookup(msg)
        Dictionary.insert(END, "Meaning: " + res + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        Dictionary.config(state=DISABLED)
        Dictionary.yview(END)
def search_kanji():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg!='':
        Dictionary.config(state=NORMAL)
        Dictionary.insert(END, "You: "+ msg + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        res =  if_kanji(msg)
        Dictionary.insert(END, "Meaning: " + res + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        Dictionary.config(state=DISABLED)
        Dictionary.yview(END)
def speak_ja(message):
    try:
        mp3_fp = BytesIO()
        speech = gTTS(text=message,lang='ja')
        speech.write_to_fp(mp3_fp)
    except Exception:
        raise
    return mp3_fp
def speak_en(message):
    try:
        mp3_fp = BytesIO()
        speech = gTTS(text=message,lang='en')
        speech.write_to_fp(mp3_fp)
    except Exception:
        raise
    return mp3_fp
def playsound_ja(patterns):
#Speak
    mixer.init()
    sound = speak_ja(patterns)
    sound.seek(0)
    mixer.music.load(sound,"mp3")
    mixer.music.play()
    time.sleep(5)
def playsound_en(patterns):
    #Speak
    mixer.init()
    sound = speak_en(patterns)
    sound.seek(0)
    mixer.music.load(sound,"mp3")
    mixer.music.play()
    time.sleep(5)
def activate_microphone_language():
    choice = variable.get()
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        speech = recognize.record(source, duration= 5)
        try:
            print("Recognizing the speech")
            speech = recognize.recognize_google(speech, language= choice)
        except Exception:
            print("Can't recognize your speech")
    smsg = str(speech)
    
    #smsg_ja = translate_to_ja(smsg)
    translator = Translator()
    translation = translator.translate(smsg,src = choice,dest = 'ja')
    #preprocess to remove unnecessary result of pygoogletranslation 
    # initializing substrings
    sub1 = "text="
    sub2 = ", pronunciation"
    # getting index of substrings
    idx1 = str(translation).index(sub1)
    idx2 = str(translation).index(sub2)
    smsg_ja = ''
    # getting elements in between
    for idx in range(idx1 + len(sub1) , idx2):
            smsg_ja = smsg_ja + str(translation)[idx]
    print("Translate from: %s"%choice)
    print(smsg)
    print('Translation results: '+smsg_ja)
    substring = '<speech_recognition.audio.AudioData object at'
    #Visualize
    if substring not in smsg_ja:
        Dictionary.config(state=NORMAL)
        Dictionary.insert(END, "You: "+ smsg + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        res =  if_kanji(smsg_ja)
        Dictionary.insert(END, "Meaning: " + res + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        Dictionary.config(state=DISABLED)
        Dictionary.yview(END)
        playsound_ja(smsg_ja)
    else:
        print("Can't recognize your speech")
def activate_navigator():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        speech = recognize.record(source, duration= 5)
        try:
            print("Recognizing the speech for navigator")
            speech = recognize.recognize_google(speech, language= 'en')
        except Exception as ex:
            print(ex)
    smsg = str(speech)
    print(smsg)
    if smsg != '':
        if (smsg == 'open handwriting') | (smsg == 'open hand writing') | (smsg== 'open handwritten') | (smsg == 'open hand written') | (smsg == 'open Hand writting') | (smsg == 'open Hand') | (smsg=='open writting')| (smsg=='handwriting')|(smsg=='Handwritting'):
            playsound_en('open handwritting')
            open_handwriting()
            
        elif (smsg == "open strokes") | (smsg == 'open draw')| (smsg=='open drawing') | (smsg == 'open drawing strokes') | (smsg == 'draw') | (smsg == 'open Draw') | (smsg =='Draw'):
            playsound_en('open drawing strokes')
            open_drawing_strokes()
            
        else:
            pass
Dictionary = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
Dictionary.config(state=DISABLED)
EntryBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
language_list = ['english',"japanese","vietnamese","korean","chinese"]
lang_code_list = ['en','ja','vi','ko','zh-CN']
variable = StringVar()
variable.set(language_list[0])
dropdown = OptionMenu(
    root,
    variable,
    *language_list
)
button1 = ttk.Button(root, text="SEARCH", command=search_entry)
button2 = ttk.Button(root,text="SEARCH KANJI", command=search_kanji)
click_btn1= PhotoImage(file='image/strokes.png')
button3 = ttk.Button(root, image= click_btn1,command = open_drawing_strokes)
click_btn2 = PhotoImage(file='image/handwritten.png')
button4 = ttk.Button(root, image= click_btn2,command = open_handwriting)
click_btn3 = PhotoImage(file='image/microphone.png')
button5 = ttk.Button(root,image = click_btn3, command= activate_microphone_language )
click_btn4 = PhotoImage(file='image/navigator.png')
button6 = ttk.Button(root,image = click_btn4, command= activate_navigator )
EntryBox.place(x=6, y=6, height = 80,width= 400)
Dictionary.place(x = 6, y = 130, height= 435, width= 540 )
button1.place(x=406, y=6, height= 40, width = 90 )
button2.place(x = 406, y = 46, height= 40, width= 90)
button3.place(x = 500, y =6 )
button4.place(x = 500, y = 45  )
button5.place(x = 106, y = 85)
button6.place(x= 450, y = 85)
dropdown.place(x=6, y= 85, height= 40, width= 100 )
root.mainloop()
