from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Input, Button, Label, Select
from database import Database
from models import Inventario

class FormInventario(ModalScreen):
    def compose(self) -> ComposeResult:
        yield Label("Agregar al inventario", id="titulo")
        yield Label("ID del vino: ")
        yield Input(id="id_vino", placeholder="Ej: 1")
        yield Label("Cantidad: ")
        yield Input(id="cantidad", placeholder="Ej: 12")
        yield Label("Ubicación: ")
        yield Input(id="ubicacion", placeholder="Ej: Estante A-3")
        yield Button("Guardar", id="guardar")
        yield Button("Cancelar", id="cancelar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancelar":
            self.dismiss()
        elif event.button.id == "guardar":
            db = Database()
            inv = Inventario(
                id=None,
                id_vino=int(self.query_one("#id_vino", Input).value),
                id_proveedor=1,
                cantidad=int(self.query_one("#cantidad", Input).value),
                ubicacion=self.query_one("#ubicacion", Input).value
            )
            db.insertar_inventario(inv)
            self.dismiss()
