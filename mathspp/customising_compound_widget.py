from textual.app import App
from textual.widget import Widget
from textual.widgets import Button, Header, Input, Label

# this is using compound widget
class LabelledInput(Widget):
    DEFAULT_CSS = """
        LabelledInput {
            height: 4;
        }
    """
    
    def __init__(self, label):
        super().__init__()
        self.label = label

    def compose(self):
        yield Label(f"{self.label}:")
        yield Input(placeholder=self.label.lower())

class MyApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield LabelledInput("Name")
        yield LabelledInput("Surname")
        yield LabelledInput("Email")
        yield Button('Click me!')

MyApp().run()
