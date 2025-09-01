# This code will open a file and read its content
'''datos = open('/Users/franciscomauricio/Git/DSA/DSA28082025/planets.csv','r')
for linea in datos:
    print(linea)
datos.close()'''

# Next code will use cvs library to read the file
'''
import csv 
with open('/Users/franciscomauricio/Git/DSA/DSA28082025/planets.csv','r') as datos:
    reader = csv.reader(datos)
    for linea in reader:
        print(linea)
datos.close()'''

'''
# The next code will use cvs library to rear a file, store each line in a list and print the list. And will print the name of planet, its rotation and orbit period
import csv
with open('/Users/franciscomauricio/Git/DSA/DSA28082025/planets.csv','r') as datos:
    reader = csv.reader(datos)
    next
    lista = list(reader)

    lista.pop(0)
    #print(lista)
    for planeta in lista:
        print(f'Planeta: {planeta[0]}, Rotacion: {planeta[3]}, Periodo Orbital: {planeta[4]}')
#datos.close() 
''' 

# The next code will search the information of a specific planet and will go line by line to find it without using the librery csv
# Planetas que nos interesan
planetas_objetivo = ["Alderaan", "Yavin 4", "Hoth", "Dagobah"]

with open("/Users/franciscomauricio/Git/DSA/DSA28082025/planets.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Saltamos el encabezado
lines = lines[1:]

for line in lines:
    parts = line.strip().split(",")
    
    # Evitamos líneas incompletas
    if len(parts) < 5:
        continue

    nombre = parts[1]
    rotacion = parts[3]
    orbita = parts[4]

    # Solo mostrar si el planeta está en nuestra lista
    if nombre in planetas_objetivo:
        try:
            rotacion = int(float(rotacion))
        except ValueError:
            rotacion = None

        try:
            orbita = int(float(orbita))
        except ValueError:
            orbita = None

        print(f"Planeta: {nombre}, Rotación: {rotacion}, Órbita: {orbita}")

        