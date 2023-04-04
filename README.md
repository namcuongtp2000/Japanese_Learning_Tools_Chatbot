# Japanese_Learning_Tools_Chatbot
# **1.Introduction**

This is a simple python application for Japanese Learners included Speech Chatbot and Handwritten Recognition features.
If you want to use my work on your projects, please REFERENCE this GITHUB link.

# **2.Installation**

python -m pip install -r requirements.txt

omz_downloader --name --handwritten-japanese-recognition-0001
  
omz_downloader --name --text-detection-0003
  
 Please make sure the following files are placed at the proper location.


./
+ chatbot_model.h5
+ words.pkl
+ classes.pkl
+ intents.json
+ chatgui_speech.py
+ chatapp.py
+ japanese_dictionary.py
+ handwritten.py  
+ data  
| + kondate_nakayosi_char_list.txt  
+ intel  
| + handwritten-japanese-recognition-0001  
| | + FP16  
| | | + handwritten-japanese-recognition-0001.xml  
| | | + handwritten-japanese-recognition-0001.bin  
| + text-detection-0003  
| | + FP16  
| | | + text-detection-0003.xml  
| | | + text-detection-0003.bin

https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-3.1.3-windows-x64-installer


# **3.Using guide**

# *3.1. Chatbot window*

Here's the chatbot window:
<img src="/img/chatbot_window.png" alt="Chatbot Window" title="Chatbot Window">

You should choose your language in dropbox first and start chatting with chatbot by typing text and click "Send Text" or speak by "Microphone" symbol EXACTLY like your language you choose at first. If you use "Microphone", you can speak some command key words to open some applications/features for example "Open dictionary","Open handwriting" or "Open drawing strokes" (just something like Cortana or Google Assistant).

Or you can typing text and  click "Summarize" to summarize your text or upload a text file or pdf file by "Upload file" to summarize your documents.

Typing in the text entry box your key words and click "Search Google" and Chatlog will response some website links for you.

Voice speaking is always turn on in default. If you don't like voice speaking, you definitely can turn off and simply chat.

Here's tutorial by visual image may help you:

<img src="/img/chatbot_guide.png" alt="Chatbot Guide" title="Chatbot Guide">

# *3.2 Japanese Dictionary Window*

Here's Japanese Dictionary Window: 

<img src="/img/dictionary_window.png" alt="Dictionary Window" title="Dictionary Window">

Similar like Chatbot Window, you should first pick your language and start typing and click "SEARCH" or speak through "Microphone symbol" EXACTLY by your choosing language. If you want to search by Japanese or Kanji, type Kanji or Japanese in text box and click "SEARCH KANJI".

Voice speaking is always turn on in default. If you don't like voice speaking, you definitely can turn off and simply chat.

You can also click in other 2 symbols to open "Drawing strokes" and "Handwriting" or you can speak command through microphone by symbol "Navigator" below "Turn on/off" button.

Your results will display Japanese (Hiragan, Katakana or Kanji) words, and its meaning in your language which you chose first and it only can search/look up words or short phrases but not can translate whole long sentences. (Because it's just a dictionary, not translator).

Here's tutorial by visual image of Japanese Dictionary may help you:

<img src="/img/dictionary_guide.png" alt="Dictionary Guide" title="Dictionary Guide">

# **4.Update/Issues:**

Add exception and pass speaking Japanese in 'japanese_dictionary_gui.py' when microphone can't recognize your speech . Error results: '<speech_recognition.audio.AudioData object at 0000x...>'

Update scan japanese from images.

Update lecture interfaces and vocabularies. Coming soon!

# **5.Reference projects:**

https://github.com/yas-sim/handwritten-japanese-ocr

https://github.com/AtomCrafty/KanjiStrokes

# **6.Contact**

Please contact me via email: namcuongtp2000@gmail.com
