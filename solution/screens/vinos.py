from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Button, Label
from database import Database
from screens.form_vino import FormVino

class VinosScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Volver")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Catálogo de Vinos", id="titulo")
        yield DataTable(id="tabla-vinos")
        yield Button("+ Agregar vino", id="btn-agregar")
        yield Footer()

    def on_mount(self) -> None:
        self.cargar_vinos()

    def cargar_vinos(self) -> None:
        tabla = self.query_one("#tabla-vinos", DataTable)
        tabla.clear(columns=True)
        tabla.add_columns("Nombre", "Tipo", "Año", "Región", "Bodega", "€/Copa")
        db = Database()
        for v in db.get_vinos():
            tabla.add_row(v.nombre, v.tipo, str(v.anio), v.region, v.bodega, str(v.precio_copa))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-agregar":
            self.app.push_screen(FormVino(), self.recargar)

    def recargar(self, resultado) -> None:
        self.cargar_vinos()