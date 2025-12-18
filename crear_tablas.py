# crear_tablas.py
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import sys

print("🛠️  CREANDO TABLAS EN LA BASE DE DATOS")
print("="*50)

# Usa la MISMA configuración que tu app
DATABASE_URL = "mysql+mysqlconnector://root@localhost/api_iei_171_n2-main"

try:
    engine = create_engine(DATABASE_URL)
    Base = declarative_base()
    
    # Definición EXACTA de la tabla usuarios (basado en tu error)
    class Usuario(Base):
        __tablename__ = 'usuarios'
        
        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        nombre = Column(String(100), nullable=False)
        usuario = Column(String(50), unique=True, nullable=False, index=True)
        email = Column(String(100), unique=True, nullable=False, index=True)
        contrasena_hash = Column(String(255), nullable=False)
        contrasena_salt = Column(String(255), nullable=False)
        fecha_creacion = Column(DateTime, default=func.now())
        activo = Column(Boolean, default=True)
    
    # Tablas adicionales comunes en APIs
    class Producto(Base):
        __tablename__ = 'productos'
        
        id = Column(Integer, primary_key=True, index=True)
        nombre = Column(String(100), nullable=False)
        descripcion = Column(Text)
        precio = Column(Integer, nullable=False)  # En centavos
        stock = Column(Integer, default=0)
        fecha_creacion = Column(DateTime, default=func.now())
    
    print("📋 Creando tablas...")
    
    # Crea TODAS las tablas
    Base.metadata.create_all(bind=engine)
    
    # Verifica que se crearon
    with engine.connect() as conn:
        result = conn.execute("SHOW TABLES")
        tablas = [t[0] for t in result.fetchall()]
        
        print(f"✅ Tablas creadas en 'api_iei_171_n2-main':")
        for tabla in tablas:
            result = conn.execute(f"DESCRIBE {tabla}")
            columnas = [c[0] for c in result.fetchall()]
            print(f"   📊 {tabla}: {', '.join(columnas)}")
    
    print("\n🎉 ¡BASE DE DATOS LISTA!")
    print("Ahora puedes ejecutar tu aplicación normalmente")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Posibles soluciones:")
    print("1. Verifica que la base 'api_iei_171_n2-main' exista")
    print("2. Ejecuta en PowerShell: mysql -u root -e 'CREATE DATABASE IF NOT EXISTS \`api_iei_171_n2-main\`'")
    print("3. O usa este comando para crear la tabla manualmente:")

    print("""
-- Ejecuta en phpMyAdmin o MySQL:
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    contrasena_salt VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_usuario (usuario),
    INDEX idx_email (email)
);
    """)

input("\nPresiona Enter para probar insertar un usuario...")

# Prueba insertar un usuario
print("\n" + "="*50)
print("🧪 PROBANDO INSERCIÓN DE USUARIO")
print("="*50)

try:
    from sqlalchemy.orm import sessionmaker
    
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    # Intenta insertar un usuario de prueba
    import bcrypt
    
    # Genera hash y salt
    password = "password123"
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    
    nuevo_usuario = Usuario(
        nombre="Usuario Prueba",
        usuario="testuser",
        email="test@example.com",
        contrasena_hash=hashed.decode(),
        contrasena_salt=salt.decode()
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    print(f"✅ Usuario insertado exitosamente!")
    print(f"   ID: {nuevo_usuario.id}")
    print(f"   Nombre: {nuevo_usuario.nombre}")
    print(f"   Usuario: {nuevo_usuario.usuario}")
    
    # Verifica que se guardó
    usuario_db = db.query(Usuario).filter_by(usuario="testuser").first()
    if usuario_db:
        print(f"✅ Usuario encontrado en BD: {usuario_db.nombre}")
    
    db.close()
    
except Exception as e:
    print(f"❌ Error al insertar: {e}")

print("\n" + "="*50)
print("🚀 AHORA EJECUTA TU APLICACIÓN")
print("El error 'table doesn't exist' debería estar solucionado")