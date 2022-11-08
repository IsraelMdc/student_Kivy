#coding=utf -8 #Serve para colocar acentos e rodar os scripts via terminal sem erro
from kivy.app import App 
from kivy.uix.button import Button

class Tela(App): 
    def build(self):
        return Button(text = 'Olá mundo!', font_size = 100)

Tela().run()
