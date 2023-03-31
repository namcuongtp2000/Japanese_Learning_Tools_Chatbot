# Japanese_Learning_Tools_Chatbot
1.Introduction

This is a simple python application for Japanese Learners included Speech Chatbot and Handwritten Recognition features.
If you want to use my work on your projects, please REFERENCE this GITHUB link.

2.Installation

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


3.Using guide

4.Update/ Fix bugs:

Add exception and pass speaking Japanese in 'japanese_dictionary_gui.py' when microphone can't recognize your speech . Error results: '<speech_recognition.audio.AudioData object at 0000x...>'

5.Reference projects:
https://github.com/yas-sim/handwritten-japanese-ocr
https://github.com/AtomCrafty/KanjiStrokes
