import sqlite3
from models import Vino, Proveedor, Inventario, Movimiento

class Database:
    def __init__(self, db_path="cava.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._crear_tablas()

    def _crear_tablas(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS vinos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                anio INTEGER,
                region TEXT,
                bodega TEXT,
                precio_copa REAL,
                precio_botella REAL   
                          )
            """)
        
            
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS proveedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                contacto TEXT,
                email TEXT,
                telefono TEXT   
                          )
            """)
    
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS inventario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_vino INTEGER,
                id_proveedor INTEGER,
                cantidad INTEGER,
                ubicacion TEXT   
                          )
            """)
    
        self.conn.execute ("""
            CREATE TABLE IF NOT EXISTS movimientos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_vino INTEGER,
                tipo TEXT,
                cantidad INTEGER,
                notas TEXT
                          )
            """)
    
        self.conn.commit()

    def get_vinos(self):
        rows = self.conn.execute("SELECT * FROM vinos").fetchall()
        return [Vino(
            id=r["id"],
            nombre=r["nombre"],
            tipo=r["tipo"],
            anio=r["anio"],
            region=r["region"],
            bodega=r["bodega"],
            precio_copa=r["precio_copa"],
            precio_botella=r["precio_botella"]
    ) for r in rows]

    def insertar_vino(self, v: Vino):
        self.conn.execute(
        """INSERT INTO vinos 
        (nombre, tipo, anio, region, bodega, precio_copa, precio_botella)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (v.nombre, v.tipo, v.anio, v.region, v.bodega, v.precio_copa, v.precio_botella)
    )
        self.conn.commit()

    def get_inventario(self):
        rows = self.conn.execute("""
            SELECT v.nombre, v.tipo, i.cantidad, i.ubicacion
            FROM inventario i
            JOIN vinos v ON i.id_vino = v.id
        """).fetchall()
        return rows
    
    def get_movimientos(self):
        rows = self.conn.execute("""
            SELECT v.nombre, m.tipo, m.cantidad, m.notas
            FROM movimientos m
            JOIN vinos v ON m.id_vino = v.id
        """)
        return rows
    
    def get_proveedores(self):
        rows = self.conn.execute("SELECT * FROM proveedores").fetchall()
        return [Proveedor(
            id=r["id"],
            nombre=r["nombre"],
            contanto=r["contacto"],
            email=r["email"],
            telefono=r["telefono"]
        )for r in rows]
    
    def insertar_inventario(self, inv: Inventario):
        self.conn.execute(
            """INSERT INTO inventario
            (id_vino, id_proveedor, cantidad, ubicacion)
            VALUES (?, ?, ?, ?)""",
            (inv.id_vino, inv.id_proveedor, inv.cantidad, inv.ubicacion)
        )
        self.conn.commit()