def solicitar_informacion():
    # Solicitar información al usuario
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    codigo_seccion = input("Ingrese su código de sección: ")
    sede = input("Ingrese su sede: ")

    # Mostrar la información ingresada en pantalla
    print("\nInformación ingresada:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Código de sección:", codigo_seccion)
    print("Sede:", sede)

# Llamada a la función para solicitar información
solicitar_informacion()