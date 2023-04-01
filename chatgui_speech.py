#Creating GUI with tkinter
import tkinter
from tkinter import *
from tkinter import messagebox as massage
from tkinter.filedialog import askopenfile
from tkinter import filedialog
from chatapp import chatbot_response
import speech_recognition as sr
#import playsound
#playsound = 1.2.2
from summa import *
from gtts import gTTS
from pygoogletranslation import Translator
from langdetect import detect
import os
from io import BytesIO
from pygame import mixer
import time
from PyPDF2 import PdfReader
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
def translate_to_en(patterns):
    #global lang_src
    
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
def translate_to_dest(patterns):
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
def translate_from_ja_to_en(patterns):
    translator = Translator()
    translation = translator.translate(patterns, src='ja',dest='en')
    sub1 = "text="
    sub2 = ", pronunciation"
    idx1 = str(translation).index(sub1)
    idx2 = str(translation).index(sub2)
    result_dest = ''
    # getting elements in between
    for idx in range(idx1 + len(sub1) , idx2):
            result_dest = result_dest + str(translation)[idx]
    print("Translate result: "+result_dest)
    return result_dest
#Input speech
def listen(duration):
    base = sr.Recognizer()
    with sr.Microphone() as source:
        text = base.record(source, duration=duration)
        try:
            print("Recognizing the text")
            return base.recognize_google(text,language="en-US")
        except Exception as ex:
            print(ex)

#Output speech voice
id = 0   	
def speak(massage):
    try:
        #lang_dest = lang_detect(massage)
        lang_dest = variable.get()
        mp3_fp = BytesIO()
        if lang_dest == "English":
            speech = gTTS(text=massage, lang= lang_dest.replace("English","en"))
            #speech.write_to_fp(mp3_fp)
        elif lang_dest == "Vietnamese":
            speech = gTTS(text=massage, lang= lang_dest.replace("Vietnamese","vi"))
            #speech.write_to_fp(mp3_fp)
        elif lang_dest == "Japanese":
            speech = gTTS(text=massage, lang= lang_dest.replace("Japanese","ja"))
            #speech.write_to_fp(mp3_fp)
        elif lang_dest == "Korean":
            speech = gTTS(text=massage, lang= lang_dest.replace("Korean","ko"))
            #speech.write_to_fp(mp3_fp)
        elif lang_dest == "French":
            speech = gTTS(text=massage, lang= lang_dest.replace("French","fr"))
            #speech.write_to_fp(mp3_fp)
        elif lang_dest == "Chinese":
            speech = gTTS(text=massage, lang= lang_dest.replace("Chinese","zh-CN"))
        
        speech.write_to_fp(mp3_fp)
        '''filename="voice_%s_%d.mp3"%(lang_dest,id)
    speech.save(filename)
    playsound.playsound(filename)'''
    except Exception:
        raise
    return mp3_fp
def playvoice(patterns):
    mixer.init()
    sound = speak(patterns)
    sound.seek(0)
    mixer.music.load(sound,"mp3")
    mixer.music.play()
    time.sleep(5)

#Function
def activate_microphone_language():
    choice = variable.get()
    base = sr.Recognizer()
    with sr.Microphone() as source:
        text = base.record(source, duration=5)
        try:
            print("Recognizing the text")
            text = base.recognize_google(text,language=choice)
        except Exception as ex:
            print(ex)
    smsg = str(text)
    smsg_en = translate_to_en(smsg)
    #global id
    #id = id+1
    print(smsg_en)
    EntryBox.insert(END, smsg)
    EntryBox.delete("0.0",END)
    if smsg_en != '':
        
        res = chatbot_response(smsg_en)
        
        #Output speaker voice
        if res =='open handwriting':
            print('Navigating to handwriting')
            playvoice('open handwriting')
            os.system('python handwritten.py')
        elif res =='open camera':
            print('Navigating to camera')
            playvoice('open camera')
            os.system('')
        elif res == 'open dictionary':
            print('Navigating to dictionary')
            playvoice('open dictionary')
            os.system('python japanese_dictionary_gui.py')
        elif res == 'OK. I will summarize your documents immediately, please wait for a second.':
            print('Navigating to summarizer.')
            playvoice('OK. Please make sure you entered your text message in text entry box before start using microphone. I will summarize your documents immediately, please wait for a second.')
            summary()
        else:
            result_trans = translate_to_dest(res)
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + smsg + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            ChatLog.insert(END, "Bot: " + str(result_trans) + '\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            #Output speaker voice
            print(result_trans)
            playvoice(str(result_trans))

def send():
    #Input
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    msg_en = translate_to_en(msg)
    
    global id
    id = id + 1
    #Execute
    if msg_en != '':
        res = chatbot_response(msg_en)
        print('response:'+res)
        result_dest = translate_to_dest(res)
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        ChatLog.insert(END, "Bot: " + result_dest + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        playvoice(str(result_dest))

def search_google():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")
        # to search
        ChatLog.insert(END, "You: " + msg + '\n\n')
        for j in search(msg, tld="co.in", num=10, stop=10, pause=2):
            print(j)
            #res = chatbot_response(msg)
            ChatLog.config(state=NORMAL)
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            ChatLog.insert(END, j + '\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

def upload_text():
    try:
        file_path=filedialog.askopenfilename()
        print(file_path)
        if str(file_path).endswith('.txt'):
            uploaded= open(file_path)
            data = uploaded.read()
            if data != '':
                ChatLog.config(state=NORMAL)
                summarization = summarizer.summarize(data)
                summarization_lang = translate_to_dest(summarization)
                ChatLog.insert(END, "Bot: " + summarization_lang + '\n\n')
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
                print(summarization_lang)
                playvoice(str(summarization_lang))
        elif str(file_path).endswith('.pdf'):
            reader = PdfReader(file_path)
            print('Your pdf file has %s pages'%len(reader.pages))
            #PyPDF2 has now not supported scanning multiple pages in the same time using PdfFileReader anymore. 
            #If you want to summarize all pages of your pdf, you can use PyMuPDF instead or just adjust the index i of pages[i] in line 'page = reader.pages[0]'
            page = reader.pages[0]
            text = page.extract_text()
            #print(text)
            if text != '':
                ChatLog.config(state=NORMAL)
                summarization = summarizer.summarize(text)
                summarization_lang = translate_to_dest(summarization)
                ChatLog.insert(END, "Bot: " + summarization_lang + '\n\n')
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
                print(summarization_lang)
                playvoice(str(summarization_lang))
        else:
            print("Your file is not pdf or text file")
        
    except:
        pass
def summary():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    #Execute
    if msg != '':
        ChatLog.config(state=NORMAL)
        summarization = summarizer.summarize(msg)
        summarization_lang = translate_to_dest(summarization)
        ChatLog.insert(END, "Bot: " + summarization_lang + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    print(summarization_lang)
    playvoice(str(summarization_lang))
    #return summarization
def open_dictionary():
    try:
        os.system('python japanese_dictionary_gui.py')
    except:
        pass
base = Tk()
base.title("Modern Chatbot")
base.geometry("1366x768")
base.resizable(width=FALSE, height=FALSE)
#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)
#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
# creating widget
language_list = ['English','Vietnamese','Japanese','French','Chinese','Korean']
# set default country as United States
variable = StringVar()
variable.set(language_list[0])
dropdown = OptionMenu(
    base,
    variable,
    *language_list,
    #command=activate_microphone_language
)
# positioning widget
dropdown.pack(expand=True)
dropdown.place(x=4, y = 420,height=40, width=100 )
#Create Button to send message
SendButton = Button(base, font=("Verdana",9,'bold'), text="Send Text", width="16", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )
SummarizerButton = Button(base, font=("Verdana",9,'bold'), text="Summarize", width="16", height=5,
                    bd=0, bg="#1E90FF", activebackground="#3c9d9b",fg='#ffffff',
                    command= summary )
UploadSummarizeButton = Button(base, font=("Verdana",9,'bold'), text="Upload file", width="16", height=5,
                    bd=0, bg="#EE2C2C", activebackground="#3c9d9b",fg='#ffffff',
                    command= upload_text )
SearchGoogleButton = Button(base, font=("Verdana",9,'bold'), text="Search Google", width="16", height=5,
                    bd=0, bg="#DEB887", activebackground="#3c9d9b",fg='#ffffff',
                    command= search_google )
DictionaryButton = Button(base, font=("Verdana",9,'bold'), text="Open dictionary", width="16", height=5,
                    bd=0, bg="#FFC125", activebackground="#3c9d9b",fg='#ffffff',
                    command= open_dictionary )
choose_language = Label(base, text= "Choose your language before start:")
choose_language.place(x = 6 ,y = 400 )
chatlog_label = Label(base, text= 'Response windows:')
chatlog_label.place(x=6,y=2)
#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)
#Place all components on the screen
click_btn1 = PhotoImage(file='image/microphone.png')
MicrophoneButton = Button(base, image=click_btn1, command= activate_microphone_language )
scrollbar.place(x=1346,y=10, height=400)
ChatLog.place(x=6,y=20, height=380, width=1345)
EntryBox.place(x=145, y=420, height=340, width=1205)
SendButton.place(x=6, y=460, height=30,width=130)
SummarizerButton.place(x=6,y=494,height=30,width= 130)
UploadSummarizeButton.place(x=6, y=530, height=30, width= 130 )
SearchGoogleButton.place(x= 6,y= 564, height= 30 ,width=130)
DictionaryButton.place(x = 6, y = 598,height=30,width= 130)
MicrophoneButton.place(x=100,y = 422)
base.mainloop()
