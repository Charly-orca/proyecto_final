import mysql.connector
# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@1976",
    database="login_rester_db"  # nombre de la base de datos
)
# Función para verificar la conexión a la base de datos
def verificar_conexion():
    try:
        # Crear un cursor para realizar una operación simple de consulta y verificar la conexión
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_completo FROM usuarios")  # Corregí la consulta
        rows = cursor.fetchall()  # Leer todos los resultados de la consulta
        cursor.close()
        #print(rows)
        return True  
    except Exception as e:
        print("Error al verificar la conexión a la base de datos:", e)
        return False
#if verificar_conexion():
    print("La conexion a la base de datos se estableció correctamente.")
#else:
    print("Error:N No se pudo establecer conexion.")
    