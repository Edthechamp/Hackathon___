from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
Builder.load_file('build.kv')
class ToDoApp(App):
    def callback(self):
        with open('data.txt', 'a') as f:
            f.write(self.root.ids.input.text + '\n')
            f.close()
        self.root.ids.input.text = ''
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    ToDoApp().run()