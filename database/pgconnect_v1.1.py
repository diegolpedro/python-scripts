#!bin/python3
#-----------------------------------------------------------------------------#
# pgconnect.py - Postgres conexion                      by Pedro, Diego  2018 #
# Version:                                                                    #
# 1.0 _ Primer implementacion. Clase para conexion.                           #
# 1.1 _ Ejecuta sentencias pasadas por parametro.                             #
#-----------------------------------------------------------------------------#
VERSION=1.1

# Importamos libreria.
import psycopg2

# Seteos de configuracion.
database = "base_db"
user = "usename"
password = "password"
host = "host"
port = "puerto"


#----------------------- Clase para menejo de conexion -----------------------
class Pgconnect:
  ''' Manejo de base de datos '''
  
  def __init__(self, database, user, password, host, port):
    ''' Constructor '''
    self.database = database
    self.user = user
    self.password = password
    self.host = host
    self.port = port

  def conectar(self):
    ''' Conexion con la base de datos '''
    self.conn = psycopg2.connect(database=self.database, user=self.user,
                                password=self.password, host=self.host,
                                port=self.port)
    # Inicializa cursor
    self.cur = self.conn.cursor()
    print("Base conectada y cursor creado.")
  
  def ejecutar(self, query):
    ''' Ejecuta sentencias enviadas por parametro'''
    self.cur.execute(query)
    result = self.cur.fetchall()
    return result

#-------------------------------- Inicio Main --------------------------------
# Generamos el objeto de conexion.
vec = Pgconnect(database, user, password, host, port)
# Conectamos.
vec.conectar()
# Ejecutamos query
rows = vec.ejecutar("SELECT * FROM tabla_t")

for row in rows:
  print("COL1 = ", row[0])
  print("COL2 = ", row[1])
  print("COL3 = ", row[2], "\n")

print("Finalizado con exito");