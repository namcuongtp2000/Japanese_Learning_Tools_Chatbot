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
root.geometry("600x600")
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
def preprocess_translate(patterns):
    #preprocess to remove unnecessary result of pygoogletranslation
    # initializing substrings
        sub1 = "text="
        sub2 = ", pronunciation"
        # getting index of substrings
        idx1 = str(patterns).index(sub1)
        idx2 = str(patterns).index(sub2)
        result = ''
        # getting elements in between
        for idx in range(idx1 + len(sub1) , idx2):
            result = result + str(patterns)[idx]
        print(result)
        return result
def translate_to_ja(patterns):
    try:
        lang_src = variable.get()
        translator = Translator()
        if lang_src == 'English':
            translation = translator.translate(patterns,src =lang_src.replace("English","en"),dest = 'ja')
        elif lang_src == 'Vietnamese':
            translation = translator.translate(patterns,src =lang_src.replace("Vietnamese","vi"),dest = 'ja')
        elif lang_src == 'Japanese':
            translation = translator.translate(patterns,src =lang_src.replace("Japanese","ja"),dest = 'ja')
        elif lang_src == 'Korean':
            translation = translator.translate(patterns,src =lang_src.replace("Korean","ko"),dest = 'ja')
        elif lang_src == 'French':
            translation = translator.translate(patterns,src =lang_src.replace("French","fr"),dest = 'ja')
        elif lang_src == 'Chinese':
            translation = translator.translate(patterns,src =lang_src.replace("Chinese","zh-CN"),dest = 'ja')
    except StopIteration:
        pass
    return preprocess_translate(translation)
def translate_to_dest(patterns):
    try:
        choice = variable.get()
        translator_dest = Translator()
        if choice == 'English':
            translation = translator_dest.translate(patterns,src = 'ja',dest = choice.replace("English","en"))
        elif choice == "Vietnamese":
            translation = translator_dest.translate(patterns,src = 'ja',dest = choice.replace("Vietnamese","vi"))
        elif choice == 'Japanese':
            translation = translator_dest.translate(patterns,src = 'ja',dest = choice.replace("Japanese","ja"))
        elif choice == 'Korean':
            translation = translator_dest.translate(patterns,src = 'ja',dest = choice.replace("Korean","ko"))
        elif choice == "French":
            translation = translator_dest.translate(patterns,src = 'ja',dest = choice.replace("French","fr"))
        else:
            translation = translator_dest.translate(patterns,src = 'ja',dest = choice.replace("Chinese","zh-CN"))
    except StopIteration:
        pass
    return preprocess_translate(translation)
def translate_to_en(patterns):
    try:
        lang_src = variable.get()
        translator = Translator()
        if lang_src == 'English':
            translation = translator.translate(patterns,src =lang_src.replace("English","en"),dest = 'en')
            #preprocess_translate(translation)
        elif lang_src == 'Vietnamese':
            translation = translator.translate(patterns,src =lang_src.replace("Vietnamese","vi"),dest = 'en')
            #preprocess_translate(translation)
        elif lang_src == 'Japanese':
            translation = translator.translate(patterns,src =lang_src.replace("Japanese","ja"),dest = 'en')
            #preprocess_translate(translation)
        elif lang_src == 'Korean':
            translation = translator.translate(patterns,src =lang_src.replace("Korean","ko"),dest = 'en')
            #preprocess_translate(translation)
        elif lang_src == 'French':
            translation = translator.translate(patterns,src =lang_src.replace("French","fr"),dest = 'en')
            #preprocess_translate(translation)
        elif lang_src == 'Chinese':
            translation = translator.translate(patterns,src =lang_src.replace("Chinese","zh-CN"),dest = 'en')
            #preprocess_translate(translation)
    except StopIteration:
        pass
    return preprocess_translate(translation)
def translate_en_to_dest(patterns):
    try:
        choice = variable.get()
        translator_dest = Translator()
        if choice == 'English':
            translation = translator_dest.translate(patterns,src = 'english',dest = choice.replace("English","en"))
            #preprocess_translate(translation)
        elif choice == "Vietnamese":
            translation = translator_dest.translate(patterns,src = 'english',dest = choice.replace("Vietnamese","vi"))
            #preprocess_translate(translation)
        elif choice == 'Japanese':
            translation = translator_dest.translate(patterns,src = 'english',dest = choice.replace("Japanese","ja"))
            #preprocess_translate(translation)
        elif choice == 'Korean':
            translation = translator_dest.translate(patterns,src = 'english',dest = choice.replace("Korean","ko"))
            #preprocess_translate(translation)
        elif choice == "French":
            translation = translator_dest.translate(patterns,src = 'english',dest = choice.replace("French","fr"))
            #preprocess_translate(translation)
        else:
            translation = translator_dest.translate(patterns,src = 'english',dest = choice.replace("Chinese","zh-CN"))
            #preprocess_translate(translation)
    except StopIteration:
        pass
    return preprocess_translate(translation)
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
    os.system('start D:\Project\JapaneseDictionary\KanjiStrokes\KanjiStrokes.exe')
def open_handwriting():
    os.system('python D:\Project\Handwritten\handwritten-japanese-ocr\handwritten.py')
def search_entry():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg!='':
        Dictionary.config(state=NORMAL)
        Dictionary.insert(END, "You: "+ msg + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        res =  word_lookup(msg)
        res_trans = translate_to_dest(res)
        translation = translate_to_ja(msg)
        Dictionary.insert(END, "Japanese: " + translation+" . Meaning: "+ res_trans + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        Dictionary.config(state=DISABLED)
        Dictionary.yview(END)
        if is_on==True:
            playsound_ja(translation)
        else:
            pass
def search_kanji():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg!='':
        Dictionary.config(state=NORMAL)
        Dictionary.insert(END, "You: "+ msg + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        res =  if_kanji(msg)
        res_trans = translate_to_dest(res)
        translation = translate_to_ja(msg)
        Dictionary.insert(END, "Japanese: " + translation+" . Meaning: "+ res_trans + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        Dictionary.config(state=DISABLED)
        Dictionary.yview(END)
        if is_on==True:
            playsound_ja(translation)
        else:
            pass
def speak(massage):
    try:
        lang_dest = variable.get()
        mp3_fp = BytesIO()
        if lang_dest == "English":
            speech = gTTS(text=massage, lang= lang_dest.replace("English","en"))
        elif lang_dest == "Vietnamese":
            speech = gTTS(text=massage, lang= lang_dest.replace("Vietnamese","vi"))
        elif lang_dest == "Japanese":
            speech = gTTS(text=massage, lang= lang_dest.replace("Japanese","ja"))
        elif lang_dest == "Korean":
            speech = gTTS(text=massage, lang= lang_dest.replace("Korean","ko"))
        elif lang_dest == "French":
            speech = gTTS(text=massage, lang= lang_dest.replace("French","fr"))
        elif lang_dest == "Chinese":
            speech = gTTS(text=massage, lang= lang_dest.replace("Chinese","zh-CN"))
        
        speech.write_to_fp(mp3_fp)
    except Exception:
        raise
    return mp3_fp
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
def playvoice(patterns):
    #Speak
    mixer.init()
    sound = speak(patterns)
    sound.seek(0)
    mixer.music.load(sound,"mp3")
    mixer.music.play()
    time.sleep(5)
is_on= True
def switch_voice():
    global is_on
    #Determine is on or off
    if is_on:
        on_button.config(image = off)
        is_on = False
    else:
        on_button.config(image = on)
        is_on = True
def activate_microphone_language():
    choice = variable.get()
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        speech = recognize.record(source, duration= 5)
        try:
            print("Recognizing the speech")
            if choice == "English":
                speech = recognize.recognize_google(speech,language=choice.replace("English","en-US"))
            elif choice == "Vietnamese":
                speech = recognize.recognize_google(speech,language=choice.replace("Vietnamese","vi"))
            elif choice == "Japanese":
                speech = recognize.recognize_google(speech,language=choice.replace("Japanese","ja"))
            elif choice == "Korean":
                speech = recognize.recognize_google(speech,language=choice.replace("Korean","ko"))
            elif choice == "French":
                speech = recognize.recognize_google(speech,language=choice.replace("French","fr"))
            elif choice == "Chinese":
                speech = recognize.recognize_google(speech,language=choice.replace("Chinese","zh-CN"))
        except Exception:
            print("Can't recognize your speech")
    smsg = str(speech)
    smsg_ja = translate_to_ja(smsg)
    print(smsg)
    #Visualize
    if smsg_ja!='':
        res =  if_kanji(smsg_ja)
        Dictionary.config(state=NORMAL)
        Dictionary.insert(END, "You: "+ smsg + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        res_trans = translate_to_dest(res)
        Dictionary.insert(END, "Japanese: "+ smsg_ja+ " . Meaning: " + res_trans + '\n\n')
        Dictionary.config(foreground="#442265", font=("Verdana", 12 ))
        Dictionary.config(state=DISABLED)
        Dictionary.yview(END)
        if is_on ==True:
            playsound_ja(smsg_ja)
        else:
            pass
    else:
        print("Can't recognize your speech")
def activate_navigator():
    choice = variable.get()
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        speech = recognize.record(source, duration= 5)
        try:
            print("Recognizing the speech for navigator")
            if choice == "English":
                speech = recognize.recognize_google(speech,language=choice.replace("English","en-US"))
            elif choice == "Vietnamese":
                speech = recognize.recognize_google(speech,language=choice.replace("Vietnamese","vi"))
            elif choice == "Japanese":
                speech = recognize.recognize_google(speech,language=choice.replace("Japanese","ja"))
            elif choice == "Korean":
                speech = recognize.recognize_google(speech,language=choice.replace("Korean","ko"))
            elif choice == "French":
                speech = recognize.recognize_google(speech,language=choice.replace("French","fr"))
            elif choice == "Chinese":
                speech = recognize.recognize_google(speech,language=choice.replace("Chinese","zh-CN"))
        except Exception as ex:
            print(ex)
    smsg = str(speech)
    smsg_trans = translate_to_en(smsg)
    print(smsg)
    print(smsg_trans)
    if smsg_trans != '':
        if (smsg_trans == 'open handwriting') | (smsg_trans == 'open hand writing') | (smsg_trans== 'open handwritten') | (smsg_trans == 'open hand written') | (smsg_trans == 'open Hand writting') | (smsg_trans == 'open Hand') | (smsg_trans=='open writting')| (smsg_trans=='handwriting')|(smsg_trans=='Handwritting'):
            playvoice(translate_en_to_dest('open handwritting'))
            open_handwriting()
            
        elif (smsg_trans == "open strokes") | (smsg_trans == 'open draw')| (smsg_trans=='open drawing') | (smsg_trans == 'open drawing strokes') | (smsg_trans == 'draw') | (smsg_trans == 'open Draw') | (smsg_trans =='Draw')| (smsg_trans=="blueprint"):
            playvoice(translate_en_to_dest('open drawing strokes'))
            open_drawing_strokes()
        else:
            pass
Dictionary = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
Dictionary.config(state=DISABLED)
EntryBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
language_list = ['English',"Japanese","Vietnamese","Korean","French","Chinese"]
#lang_code_list = ['en','ja','vi','ko','zh-CN','fr']
variable = StringVar()
variable.set(language_list[0])
dropdown = OptionMenu(
    root,
    variable,
    *language_list
)
scrollbar = Scrollbar(root, command=Dictionary.yview, cursor="heart")
Dictionary['yscrollcommand'] = scrollbar.set
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
choose_language = Label(root, text='Choose your language before start:')
choose_language.place(x= 6, y =4)
search_result = Label(root, text='Search results:')
search_result.place(x= 6, y = 160)
voice_label = Label(root, text='Turn on/off voice:')
voice_label.place(x= 400, y = 8)
navigator = Label(root, text= 'Microphone navigator:')
navigator.place(x = 432, y = 45)
scrollbar.place(x= 580, y= 180, height=410)
EntryBox.place(x=6, y=80, height = 80,width= 500)
Dictionary.place(x = 6, y = 185, height= 410, width= 580 )
button1.place(x=506, y=80, height= 40, width = 90 )
button2.place(x = 506, y = 120, height= 40, width= 90)
button3.place(x = 145, y =25 )
button4.place(x = 185, y = 25  )
button5.place(x = 106, y = 25)
button6.place(x= 560, y = 40)
dropdown.place(x=6, y= 25 , height= 40, width= 100 )
on = PhotoImage(file='image/on.png')
off = PhotoImage(file='image/off.png')
on_button = Button(root, image = on, bd = 0,command = switch_voice)
on_button.place(x = 500 , y= 0)
root.mainloop()