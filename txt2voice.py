from gtts import gTTS
import os
mytext = 'Python Cycle Two Review'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")