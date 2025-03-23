from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    
    MDLabel:
        text: 'Hello World'
        pos_hint: {'center_y': .5}
        halign: 'center'
'''


class MainApp(MDApp):

    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    MainApp().run()
