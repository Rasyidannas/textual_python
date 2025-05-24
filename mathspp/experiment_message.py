from textual.app import App
from textual.widget import Widget
from textual.message import Message
from textual.widgets import Button, Label

class SoundMessage(Message):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

class SoundButton(Widget):
    DEFAULT_CSS="""
    SoundButton{
        height: 5;
    }
    """

    def compose(self):
        yield Button("Activate Sound!")

    def on_button_pressed(self):
        # this will send a message with name SoundMessage
        self.post_message(SoundMessage(sound="Meow"))

class MyApp(App):
    def compose(self):
        yield SoundButton()

    # this is will listen the SoundMessage message
    def on_sound_message(self, message: SoundMessage):
        self.mount(Label(f"Sound now: {message.sound}"))

MyApp().run()
