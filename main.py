import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.0')

class yeah(App):
    def build(self):
        return Label(text="workin type beat")

yeah = yeah()
yeah.run()