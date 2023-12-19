import 
as plt

passwords = {}

def guardar_contraseña(sitio, usuario, contraseña):
    if sitio not in passwords:
        passwords[sitio] = {'usuario': usuario, 'contraseña': contraseña}
        print(f"Contraseña para '{sitio}' guardada exitosamente.")
    else:
        print(f"Ya existe una contraseña guardada para '{sitio}'.")

def obtener_contraseña(sitio):
    if sitio in passwords:
        return passwords[sitio]
    else:
        return None

def mostrar_contraseñas():
    if passwords:
        print("Contraseñas guardadas:")
        for sitio, credenciales in passwords.items():
            print(f"Sitio: {sitio}, Usuario: {credenciales['usuario']}, Contraseña: {credenciales['contraseña']}")
    else:
        print("No hay contraseñas guardadas.")

def grafico_contraseñas():
    if passwords:
        sitios = list(passwords.keys())
        cantidades = [len(passwords[sitio]) for sitio in sitios]

        plt.bar(sitios, cantidades)
        plt.xlabel('Sitio')
        plt.ylabel('Cantidad de contraseñas')
        plt.title('Cantidad de contraseñas por sitio')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No hay contraseñas guardadas.")

# Ejemplo de uso
guardar_contraseña('ejemplo.com', 'usuario123', 'contraseña123')
guardar_contraseña('otroejemplo.com', 'admin', 'admin123')

print("--- Mostrar contraseñas ---")
mostrar_contraseñas()

print("--- Mostrar gráfico ---")
grafico_contraseñas()