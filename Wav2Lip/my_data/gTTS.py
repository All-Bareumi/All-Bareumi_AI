import speech_recognition as sr
from gtts import gTTS
import playsound


def speak(text):

     tts = gTTS(text=text, lang='ko')

     filename='school_audio.wav'

     tts.save(filename)

     playsound.playsound(filename)


speak("오늘 나는 학교에 다녀왔어요. 나는 너무 신나요.")

