# Japanese Learning Tools' Chatbot
# **1.Introduction**

This is a simple python application for Japanese Learners included Speech Chatbot and Handwritten Recognition features.
If you want to use my work on your projects, please REFERENCE this GITHUB link.

https://github.com/namcuongtp2000/Japanese_Learning_Tools_Chatbot

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

Here's the chatbot window by running "python chatgui_speech.py":
<img src="/img/chatbot_window.png" alt="Chatbot Window" title="Chatbot Window">

You should choose your language in dropbox first and start chatting with chatbot by typing text and click "Send Text" or speak by "Microphone" symbol EXACTLY like your language you choose at first. If you use "Microphone", you can speak some command key words to open some applications/features for example "Open dictionary","Open handwriting" or "Open drawing strokes" (just something like Cortana or Google Assistant).

Or you can typing text and  click "Summarize" to summarize your text or upload a text file or pdf file by "Upload file" to summarize your documents.

Typing in the text entry box your key words and click "Search Google" and Chatlog will response some website links for you.

Voice speaking is always turn on in default. If you don't like voice speaking, you definitely can turn off and simply chat.

Here's tutorial by visual image may help you:

<img src="/img/chatbot_guide.png" alt="Chatbot Guide" title="Chatbot Guide">

NOTES: There are about 250 topics and most of them talk about Japan and Japanese, may be chatbot will make some mistakes and talk about something else doesn't match with your input messages but please give it a try.

# *3.2 Japanese Dictionary Window*

Here's Japanese Dictionary Window by running "python japanese_dictionary.py": 

<img src="/img/dictionary_window.png" alt="Dictionary Window" title="Dictionary Window">

Similar like Chatbot Window, you should first pick your language and start typing and click "SEARCH" or speak through "Microphone symbol" EXACTLY by your choosing language. If you want to search by Japanese or Kanji, type Kanji or Japanese in text box and click "SEARCH KANJI".

Voice speaking is always turn on in default. If you don't like voice speaking, you definitely can turn off and simply chat.

You can also click in other 2 symbols to open "Drawing strokes" and "Handwriting" or you can speak command through microphone by symbol "Navigator" below "Turn on/off" button.

Your results will display Japanese (Hiragan, Katakana or Kanji) words, and its meaning in your language which you chose first and it only can search/look up words or short phrases but not can translate whole long sentences. (Because it's just a dictionary, not translator).

Here's tutorial by visual image of Japanese Dictionary may help you:

<img src="/img/dictionary_guide.png" alt="Dictionary Guide" title="Dictionary Guide">

# *3.3 Handwritting Window*

Thanks to https://github.com/yas-sim/handwritten-japanese-ocr, I modified a little bit in source code to make it more features for you.

Here's Japanese Handwritting Recognition Window by running "python handwritten.py":

<img src="/img/Handwritting_window.png" alt="Handwritting Window" title="Handwritting Window">

It's easy, you just draw Kanji or Japanese in white space and click "Recognize", it will response you by Japanese words, it's meaning in English and also speak it in Japanese. After that, you can click Left mouse to contunue and click "Clear" to clear space and continue draw. Moreover, you can set 2 options above: Link and Classic to adjust your pen.

You can check or copy its text and looking up results in the Terminal or CMD.

Here's an example result:

<img src="/img/Handwritting_result.png" alt="Handwritting Result" title="Handwritting Result">


# **4.Update/Current Issues:**

# 4.1 Current issues

For now, I just supported 6 languages as following: English, Vietnamese, Japanese, Korean, French and Chinese. Sorry you guys but I'm lazy to put more if/else in my code, it's because I'm just a newbie. If I made any mistakes, I will try to correct, optimize my algorithms and practice my coding skills more and more.

Add exception and pass speaking Japanese in 'japanese_dictionary_gui.py' when microphone can't recognize your speech . Error results: '<speech_recognition.audio.AudioData object at 0000x...>'

Sometimes, Google APIs such as speech_recognition(Speech to text) or gTTS(text to speech) required you must have a good and stable internet connection. You should make sure you're online to use these features. Or you can replace Google APIs Speech to Text or Text to Speech (Natural Voice Speakers) by other providers may make this app better (however, you must pay to use most of them).

Handwritten.py sometimes will make mistakes detecting too many anchor boxes and will not recognize your handwritting, it's not complete like Google Handwritting so please try to write as neat as possible.

# 4.2 Update

Update scan japanese from images.

Update lecture interfaces and vocabularies. Coming soon!

# **5.Reference projects:**

https://github.com/yas-sim/handwritten-japanese-ocr

https://github.com/AtomCrafty/KanjiStrokes

# **6.Contact**

Please contact me via email: namcuongtp2000@gmail.com
