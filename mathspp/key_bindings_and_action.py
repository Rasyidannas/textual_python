from textual.app import App
from textual.widgets import Footer, Label

class MyApp(App):
    BINDINGS = [("b", "bell", "Ring")]

    def compose(self):
        yield Footer()

    # this is an action and have to start wiht "action_"
    def action_bell(self):
        self.bell()
        self.mount(Label("Ring!"))

MyApp().run()
