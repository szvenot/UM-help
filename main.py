from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button

class UM(Screen):
    pass

class Bullseye(Screen):
    pass

class Daredevil(Screen):
    pass

class DrEllieSattler(Screen):
    pass

class Elektra(Screen):
    pass

class GhostRider(Screen):
    pass

class LukeCage(Screen):
    pass

class MoonKnight(Screen):
    pass

class TRex(Screen):
    pass

class UMApp(App):
    def build(self):
        self.icon = "HUUM.png"
        sm = ScreenManager()
        sm.add_widget(UM(name='main'))
        sm.add_widget(Bullseye(name='bullseye'))
        sm.add_widget(Daredevil(name='daredevil'))
        sm.add_widget(DrEllieSattler(name='drelliesattler'))
        sm.add_widget(Elektra(name='elektra'))
        sm.add_widget(GhostRider(name='ghostraider'))
        sm.add_widget(LukeCage(name='lukecage'))
        sm.add_widget(MoonKnight(name='moonknight'))
        sm.add_widget(TRex(name='trex'))

        return sm

if __name__=='__main__':
    UMApp().run()