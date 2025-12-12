import sqlite3

class Database:
    def __init__(self, db_name='app.db'):
        self.db_name = db_name
        self.init_db()
    
    def get_connection(self):
        """Crear conexión a la base de datos"""
        return sqlite3.connect(self.db_name)
    
    def init_db(self):
        """Inicializar la base de datos con las tablas necesarias"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Habilitar foreign keys en SQLite
        cursor.execute('PRAGMA foreign_keys = ON')
        
        # Tabla PRODUCTS
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK(price >= 0),
                stock INTEGER NOT NULL CHECK(stock >= 0),
                category TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla SALES
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                total REAL NOT NULL CHECK(total >= 0),
                sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products(id)
                    ON DELETE RESTRICT
                    ON UPDATE CASCADE
            )
        ''')
        
        # Tabla PAYMENTS
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sale_id INTEGER NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                payment_method TEXT NOT NULL CHECK(payment_method IN ('Cash', 'Yape', 'Transfer')),
                status TEXT NOT NULL CHECK(status IN ('Pending', 'Cancelled')) DEFAULT 'Pending',
                payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (sale_id) REFERENCES sales(id)
                    ON DELETE RESTRICT
                    ON UPDATE CASCADE
            )
        ''')

        conn.commit()
        conn.close()
        
        print("✅ Base de datos inicializada correctamente")

    def get_products(self):
        """Obtener todos los productos"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        conn.close()
        return products
    
    def add_product(self, name, price, stock, category):
        """Agregar un nuevo producto"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO products (name, price, stock, category)
            VALUES (?, ?, ?, ?)
        ''', (name, price, stock, category))
        conn.commit()
        conn.close()
        
        print(f"✅ Producto '{name}' agregado correctamente")

# Inicializar la base de datos
if __name__ == "__main__":
    db = Database()