from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.window.add_widget(Label(text="paruski"))
        #add widgets to window

        self.user = TextInput()
        self.window.add_widget(self.user)

        self.button = Button(text="Hello")
        self.window.add_widget(self.button)


        return self.window

if __name__ == "__main__":
    SayHello().run()