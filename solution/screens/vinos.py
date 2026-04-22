from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Button, Label
from database import Database

class VinosScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Volver")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Catálogo de Vinos", id="titulo")
        yield DataTable (id="tabla-vinos")
        yield Button ("+ Agregar vino", id="btn-agregar")
        yield Footer()

    def _on_mount(self, event) -> None:
        tabla = self.query_one("#tabla-vinos", DataTable)
        tabla.add_columns("Nombre", "Tipo", "Año", "Región", "Bodega", "€/Copa")
        db = Database()
        for v in db.get_vinos():
            tabla.add_row(v.nombre, v.tipo, str(v.anio), v.region, v.bodega, str(v.precio_copa))