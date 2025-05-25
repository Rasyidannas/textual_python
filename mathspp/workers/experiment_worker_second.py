import httpx

from textual import work
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Static

class DictionaryApp(App):
    """App to Increase Vocabulary"""

    def compose(self):
        yield Input(placeholder="Write a word")
        yield Static(id="word")
        yield Static(id="meaning")

    def on_input_changed(self, message):
        # self.mount(Static(f"{message.value}"))
        self.get_word(message.value)

# [0].meanings[0].definitions[0].definition

    @work(thread=True)
    async def get_word(self, word):
        """Get measing of a word"""
        static_word = self.query_one("#word")
        static_mean = self.query_one("#meaning")
        if word:
            url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                data = response.json()
                data_word = data[0].get('word', "")
                if data_word:
                    static_word.update(data[0].get('word', ""))
                    static_mean.update(data[0].get('meanings', [])[0].get('definitions', [])[0].get('definition', ""))
                else:
                    static_word.update(data.get("title", ""))
if __name__ == "__main__":
    app = DictionaryApp()
    app.run()
