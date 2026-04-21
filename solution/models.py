from dataclasses import dataclass

@dataclass
class Vino:
    id:  int | None
    nombre: str
    tipo: str
    anio: int
    region: str
    bodega: str
    precio_copa: float
    precio_botella: float

@dataclass
class Proveedor:
    id:  int | None
    nombre: str
    contanto: str
    email: str
    telefono: str

@dataclass
class Inventario:
    id:  int | None
    id_vino: int
    id_proveedor: int
    cantidad: int
    ubicacion: str

@dataclass
class Movimiento:
    id:  int | None
    id_vino: int
    tipo: str
    cantidad: int
    notas: str





