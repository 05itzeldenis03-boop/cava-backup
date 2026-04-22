from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Label
from database import Database

class InventarioScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Volver")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Inventario de la Cava", id="titulo")
        yield DataTable(id="tabla-inventario")
        yield Footer()


    def _on_mount(self) -> None:
        tabla = self.query_one("#tabla-inventario", DataTable)
        tabla.add_columns("Vino", "Tipo", "Cantidad", "Ubicación")
        db = Database()
        for item in db.get_inventario():
            tabla.add_row(
                item["nombre"],
                item["tipo"],
                str(item["cantidad"]),
                item["ubicación"]
            )