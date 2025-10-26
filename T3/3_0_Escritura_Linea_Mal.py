

datos = "Hola, Mundo, \n"
fichero = 'ejemplo0.csv'

with open(fichero, mode='w', newline="\n") as f:
    escritor_csv = f.write(datos)

