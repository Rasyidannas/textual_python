from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Label
from textual.reactive import reactive
from textual.containers import VerticalScroll

class Result(Label):
    result = reactive("You didn't Login!")

    def watch_result(self, result: str) -> None:
        self.update(result)

class EmailInput(VerticalScroll):
    email = reactive("")

    def compose(self) -> ComposeResult:
        yield Label("Email")
        yield Input(placeholder="Enter your email address", id="email_input")
        yield Result(id="result_label")

    def on_input_changed(self, event: Input.Changed) -> None:
        self.email = event.value
        result_label = self.query_one(Result)
        if self.email:
            result_label.result = f"Email: {self.email}"
        else:
            result_label.result = "You didn't Login!"

class LoginFormApp(App):
    """Login Form App"""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield EmailInput()

if __name__ == "__main__":
    app = LoginFormApp()
    app.run()
