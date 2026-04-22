from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from screens.vinos import VinosScreen
from screens.inventario import InventarioScreen
from screens.movimientos import MovimientosScreen

class CavaApp(App):

    SCREENS = {"vinos": VinosScreen}
    CSS = """
    Screen {
        background: #1a1a2e
    }
    """
    BINDINGS = [
        ("v", "ir_vinos", "Vinos"),
        ("i", "ir_inventario", "Inventario"),
        ("m", "ir_movimientos", "Movimientos"),
        ("q", "quit", "Salir"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_ir_vinos(self) -> None:
        self.push_screen(VinosScreen())

    def action_ir_inventario(self) -> None:
        self.push_screen(InventarioScreen())

    def action_ir_movimientos(self) -> None:
        self.push_screen(MovimientosScreen())

if __name__ == "__main__":
    app = CavaApp()
    app.run()