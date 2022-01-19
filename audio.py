import speech_recognition as sr
from recorder import Recorder
import os


#Funcao responsavel por ouvir e reconhecer a fala
def voice_to_text():
    beep = lambda x: os.system("echo -n '\a';sleep 0.5;" * x)
    beep(3)
    r = Recorder()
    r.record(2, output='out.wav') 
    r = sr.Recognizer()

    with sr.AudioFile("out.wav") as source:
        audio = r.record(source)
        try:
            s = r.recognize_google(audio, language='pt-BR')
            # print("Text: "+s)
            return s
        except Exception as e:
            print("Exception: "+str(e))
            return "erro"