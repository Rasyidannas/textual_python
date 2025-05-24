from textual import work
from textual.app import App
from textual.widgets import Button, Input, Label

class MyApp(App):
    def compose(self):
        yield Input(placeholder="filepath")
        yield Button("Load!")

    def on_button_pressed(self):
        filepath = self.query_one(Input).value
        self.load_data(filepath)

    @work(thread=True)
    def load_data(self, filepath):
        with open(filepath, "r") as f:
            for line in f:
                self.call_from_thread(self.mount, Label(line.strip()))

MyApp().run()
