from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from screens.vinos import VinosScreen

class CavaApp(App):

    SCREENS = {"vinos": VinosScreen}
    CSS = """
    Screen {
        background: #1a1a2e
    }
    """
    BINDINGS = [
        ("v", "ir_vinos", "Vinos"),
        ("q", "quit", "Salir"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_ir_vinos(self) -> None:
        self.push_screen(VinosScreen())

if __name__ == "__main__":
    app = CavaApp()
    app.run()