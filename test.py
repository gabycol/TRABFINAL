file = open("archivo.txt","a")
while True:
plataforma = input()
usuario = input()
clave = input()
file.write(f"{plataforma}-{usuario}-{clave}\n")

file = open("archivo.txt","r")

data = file.readlines()
print(data)

for i in range(len(data)):

    linea = data[i]
    lista_linea = linea.split("/")
    
    plataforma = linea[0]
    user = linea[1]
    password = linea[2]


