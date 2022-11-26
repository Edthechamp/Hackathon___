from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class SayHello(App):
    def callback(self, instance):
        print(self.user.text)

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.label = Label(text="ToDo List:")
        self.window.add_widget(self.label)
        #add widgets to window

        self.user = TextInput()
        self.window.add_widget(self.user)

        self.button = Button(text="Add task:")
        self.button.pos
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)


        return self.window

if __name__ == "__main__":
    SayHello().run()