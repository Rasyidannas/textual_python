from textual.app import App
from textual.reactive import reactive
from textual.widgets import Button, Label

class MyApp(App):
    counter = reactive(0)

    def compose(self):
        self.label = Label()
        yield self.label
        yield Button("+1")

    def on_button_pressed(self):
        self.counter += 1

    def watch_counter(self):
        """Called when the counter updated."""
        self.label.update(str(self.counter))

MyApp().run()
