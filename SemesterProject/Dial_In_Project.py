from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar


BUT_1 = '''
MDScreen:

    MDRoundFlatButton:
        text: "Press Here"
        text_color: 0, 1, 0, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press: print("abcd")
        

'''

class app(MDApp):
    def build(self):
        Window.size = (375,812)

        return Builder.load_string(BUT_1)





app().run()





