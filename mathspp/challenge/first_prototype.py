from textual.app import App
from textual.widgets import Label, Footer
from textual.widget import Widget

class TodoItem(Widget):
    DEFAULT_CSS = """
        TodoItem {
            height: 2;
        }
    """

    def compose(self):
        yield Label("I should get this done!")
        yield Label("dd/mm/yyyy")

class MyApp(App):
    BINDINGS = [("N", "new_item", "New")]

    def compose(self):
        yield Footer()

    def action_new_item(self):
        self.mount(TodoItem())

MyApp().run()
