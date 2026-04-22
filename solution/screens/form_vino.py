from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Input, Button, Label
from database import Database
from models import Vino

class FormVino(ModalScreen):
    def compose(self) -> ComposeResult:
        yield Label("Agregar vino", id="titulo")
        yield Label("Nombre:")
        yield Input(id="nombre", placeholder="Ej: Ribera del Duero")
        yield Label("Tipo:")
        yield Input(id="tipo", placeholder="Tinto, Blanco, Rosado, Espumoso")
        yield Label("Año:")
        yield Input(id="anio", placeholder="Ej: 2020")
        yield Label("Región:")
        yield Input(id="region", placeholder="Ej: Castilla")
        yield Label("Bodega:")
        yield Input(id="bodega", placeholder="Ej: Vega Sicilia")
        yield Label("Precio copa:")
        yield Input(id="precio_copa", placeholder="Ej: 4.50")
        yield Label("Precio botella:")
        yield Input(id="precio_botella", placeholder="Ej: 25.00")
        yield Button("Guardar", id="guardar")
        yield Button("Cancelar", id="cancelar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancelar":
            self.dismiss()
        elif event.button.id == "guardar":
            db = Database()
            vino = Vino(
                id=None,
                nombre=self.query_one("#nombre", Input).value,
                tipo=self.query_one("#tipo", Input).value,
                anio=int(self.query_one("#anio", Input).value),
                region=self.query_one("#region", Input).value,
                bodega=self.query_one("#bodega", Input).value,
                precio_copa=float(self.query_one("#precio_copa", Input).value),
                precio_botella=float(self.query_one("#precio_botella", Input).value)
            )
            db.insertar_vino(vino)
            self.dismiss()