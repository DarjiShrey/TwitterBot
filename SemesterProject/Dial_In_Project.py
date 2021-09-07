from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton



BUT_1 = '''
MDScreen:

    

    MDRoundFlatButton:
        text: "Press Here"
        text_color: 0, 1, 0, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.5}    
        on_release: app.show_alert_dialog()
        

'''

class app(MDApp):
    dialog = None

    def build(self):
        Window.size = (375,812)

        return Builder.load_string(BUT_1)
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="DISCARD", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()







app().run()





