#---------- Pandas ----------
#pip install pandas
import pandas as pd

#(DataFrame):
datos = {
    "Nombre": ["Ana", "Juan", "Carlos"],
    "Edad": [25, 30, 35],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
}

df = pd.DataFrame(datos)
print(df)

#(Archivo CSV):
df = pd.read_csv("datos.csv") 
print(df.head())

#(Filtrar Datos):
mayores_de_30 = df[df["Edad"] > 30]
print(mayores_de_30)