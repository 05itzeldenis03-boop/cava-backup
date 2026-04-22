from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Button, Label
from database import Database

class MovimientosScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Volver")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Movimientos de la cava", id="titulo")
        yield DataTable (id="tabla-movimientos")
        yield Footer()

    def _on_mount(self) -> None:
        tabla =  self.query_one("#tabla-movimientos", DataTable)
        tabla.add_columns("Vino", "Tipo", "Cantidad", "Notas")
        db = Database()
        for m in db.get_movimientos():
            tabla.add_row(
                m["nombre"],
                m["tipo"],
                str(m["cantidad"]),
                m["notas"] or ""
            )