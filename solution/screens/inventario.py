from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Label, Button
from database import Database
from screens.form_inventario import FormInventario

class InventarioScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Volver")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Inventario de la Cava", id="titulo")
        yield DataTable(id="tabla-inventario")
        yield Button("+ Agregar al inventario", id="btn-agregar")
        yield Footer()
    
    def on_mount(self) ->None:
        self.cargar_inventario()

    def _on_mount(self) -> None:
        tabla = self.query_one("#tabla-inventario", DataTable)
        tabla.add_columns("Vino", "Tipo", "Cantidad", "Ubicación")
        db = Database()
        for item in db.get_inventario():
            tabla.add_row(
                item["nombre"],
                item["tipo"],
                str(item["cantidad"]),
                item["ubicacion"]
            )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-agregar":
            self.app.push_screen(FormInventario(), self.recargar)
    
    def recargar(self, resultado) -> None:
        self.cargar_inventario()