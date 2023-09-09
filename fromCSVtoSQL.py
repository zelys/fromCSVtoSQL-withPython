# Analizar tipos de datos y concatenar las filas
def analizar_filas(filas):
    registros = ""
    for i in range(len(filas)):
        registros += "("
        for j in range(len(filas[i])):
            if j == len(filas[j]) - 1:
                if i == len(filas) - 1:
                    if filas[i][j].strip().isdigit():
                        registros += filas[i][j].strip() + ");"
                    else:
                        registros += "'" + filas[i][j].strip() + "');"
                elif filas[i][j].strip().isdigit():
                    registros += filas[i][j].strip() + "),\n"
                else:
                    registros += "'" + filas[i][j].strip() + "'),\n"
            elif filas[i][j].strip().isdigit():
                registros += filas[i][j].strip() + ", "
            elif type(filas[i][j].strip()) == str:
                registros += "'" + filas[i][j].strip() + "', "
    return registros


# -------------------------------------------------------------
# Metodo para medir el tiempo de ejecucion
import time

inicio = time.time()

# Abrir el archivo csv
import csv

# Ingresar el nombre del archivo csv
archivo_csv = open("Medicos.csv", "r")

registros = archivo_csv.readlines()

filas = []
# Crear arreglo con las filas de la tabla
for fila in registros:
    filas.append(fila.split(";"))

# Tomar los atributos en la variable y borrar la primera fila
campos = filas.pop(0)

with open(f"Querry.sql", "w") as consulta_sql:
    consulta_sql.write(
        f'INSERT INTO ({", ".join(campos).strip()})\nVALUES\n{analizar_filas(filas)}'
    )

# Resultado del tiempo de ejecucion
fin = time.time()
print(fin - inicio)
