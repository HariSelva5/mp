from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = {300,500}

KV="""
BoxLayout:
    orientation:"vertical"
    md_bg_color: 0, 1, 0, 1
    MDToolbar:
        
        title:"HUT"
        left_action_items: [["menu", lambda x: x]]
        on_action_button: app.callback(self.icon)
        right_action_items: [["magnify", lambda x: x]]
        on_action_button: app.callback(self.icon)
        icon_color: 0, 1, 0, 1
    MDBottomNavigation:
        panel_color: .2, .2, .2, 1
  


        MDBottomNavigationItem:
            name:"screen1"
            text: 'Wishlist'
            icon: 'heart'

            MDLabel:
                text: 'wishlist'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Menu'
            icon: 'home'

            MDLabel:
                text: 'menu'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Chat'
            icon: 'chat'

            MDLabel:
                text: 'chat'
                halign: 'center'
"""
      

class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(KV)

            

Test().run()
