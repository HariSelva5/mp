from kivy.lang import Builder

from kivymd.app import MDApp

KV = """
#:import SweetAlert kivymd_extensions.sweetalert.SweetAlert


MDScreen:

    MDRaisedButton:
        text: "EXAMPLE"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release:
            SweetAlert(window_control_buttons="mac-style").fire("Any fool can use a computer!")
"""


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    MainApp().run()