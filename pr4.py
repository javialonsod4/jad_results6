import pandas as pd
import mysql.connector

# Conectar a la base de datos RDS
mydb = mysql.connector.connect(
  host="jaddb.cmtu6ejlnowu.us-east-1.rds.amazonaws.com",
  user="admin",
  password="jaddb-password",
  database="jaddb"
)

# Leer el archivo CSV desde S3 (ajusta la ruta y el bucket)
df = pd.read_csv('s3://jad-f-results-bucket/results.csv')

# Crear la tabla si no existe
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS victorias (equipo VARCHAR(255), victorias INT)")

# Insertar los datos en la tabla
for index, row in df.iterrows():
    equipo = row['home_team']
    #victorias = row['victorias']
    sql = "INSERT INTO victorias (equipo, victorias) VALUES (%s, 1)"
    val = (equipo) #, victorias)
    mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")
