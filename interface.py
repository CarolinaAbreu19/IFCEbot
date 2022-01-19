import tkinter as tk #sudo apt-get install python3.6-tk
from tkinter import ttk
from tkinter import *
from functools import partial

import time
import os

import IFCEbot
import audio

# Classe que cria o frame do histórico com scrool
class ScrollableFrame(ttk.Frame): 
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, bg='#ffffff')        
        
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

def conversa_com_bot(minha_fala):
    if(IFCEbot.greeting(minha_fala) !=None):
        
        lb1 = tk.Label(frame1.scrollable_frame, 
                   text = '', 
                   bg='#b7b3a1',
                   wraplength=380)
        lb1['text'] = 'Você: ' + minha_fala
        lb1.pack(side=TOP) #esse label vai pro histórico
        
        lb2 = tk.Label(frame1.scrollable_frame, 
                    text = 'Test', 
                    bg='#ffb140',
                    wraplength=380)

        lb2['text'] = 'Bot: ' + IFCEbot.greeting(minha_fala) 
        lb2.pack(side=TOP) ##esse label vai pro histórico
        
        lb['text'] = IFCEbot.greeting(minha_fala)
        et.delete(0,END)

    else:
        
        lb1 = tk.Label(frame1.scrollable_frame, 
                   text = '', 
                   bg='#b7b3a1',
                   wraplength=380)
        lb1['text'] = 'Você: ' + minha_fala
        lb1.pack(side=TOP) #esse label vai pro histórico
        
        lb2 = tk.Label(frame1.scrollable_frame, 
                    text = 'Test', 
                    bg='#ffb140',
                    wraplength=380)
        lb2['text'] = 'Bot: ' + IFCEbot.response(minha_fala) # Aqui é onde coloco a resposta do chatterbot
        lb2.pack(side=TOP) ##esse label vai pro histórico
        
        lb['text'] = IFCEbot.response(minha_fala) #vai pro balão
        et.delete(0,END)

def resposta(event): #ação do botão submit
    conversa_com_bot(mystring.get()) 


def resposta_audio(event): #ação do botão submit
    texto = audio.voice_to_text()
    conversa_com_bot(texto) 
    
    
def update(ind): #função pra rodar o gif na tela
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

root = Tk()
root.configure(background='black')
root.geometry('1110x417')
root.resizable(width=0, height=0)
root.title('Chat Bot')
root.bind('<Return>', resposta)

mystring =tk.StringVar(root)

#tela com o histórico
frame1 = ScrollableFrame(root)
frame1.pack(side=RIGHT)

#gif
frameCnt = 28 # Quantidade de frames do gif
frames = [PhotoImage(file='ifcebot.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
label = Label(root)
label.place(x=0, y=0)

#saida de texto (resposta)
lb = tk.Label(root, 
                   text = 'Olá! Sou o IFCEbot. Estou aqui para responder suas perguntas sobre o IFCE!\nDigite <ajuda>, <help> ou <temas> a qualquer momento para saber com o que posso te ajudar', 
                   bg='white',
                   wraplength=315)
lb.place(x=300, y=10)

#entrada de texto
et = tk.Entry(root, 
                   width=50, 
                   textvariable = mystring, 
                   bd = 5)
et.place(x=0, y=390)

#botão enviar texto
bt = tk.Button(root, 
                    text='Enviar', 
                    fg='#000000', 
                    bg= '#ffb140',
                    height = 1, 
                    width = 10,
                    border=None,
)                  

bt.bind('<Button-1>', resposta)
bt.place(x=410, y=390)

#botão som
bt_audio = tk.Button(root, 
                    text='Gravar', 
                    fg='#000000', 
                    bg= '#ffb140',
                    height = 1, 
                    width = 10,
                    border=None,
)                  

bt_audio.bind('<Button-1>', resposta_audio)
bt_audio.place(x=520, y=390)

frame = Frame(root,
             width=200)
frame.pack()

root.after(0, update, 0)

root.mainloop()
