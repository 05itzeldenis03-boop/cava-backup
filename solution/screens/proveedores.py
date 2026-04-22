from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Label
from database import Database

class ProveedoresScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Volver")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Proveedores", id="titulo")
        yield DataTable (id="tabla-proveedores")
        yield Footer()

    def _on_mount(self) -> None:
        tabla = self.query_one("#tabla-proveedores", DataTable)
        tabla.add_columns("Nombre", "Contacto", "Email", "Teléfono")
        db = Database()
        for p in db.get_proveedores():
            tabla.add_row(
                p.nombre,
                p.contacto,
                p.email,
                p.telefono
            )
