import datetime

# Diccionario para almacenar usuarios y sus membresías
usuarios = {}

# Función para registrar un nuevo usuario ##Requisito funcional #1
def registrar_usuario(id_usuario, nombre, correo, direccion, telefono):
    if id_usuario in usuarios:
        return f"Usuario con ID {id_usuario} ya está registrado."
    
    usuarios[id_usuario] = {
        'nombre': nombre,
        'correo': correo,
        'direccion': direccion,
        'telefono': telefono,
        'membresia': 'activa',  # El estado inicial es 'activa'
        'registro_ingreso': [],
        'tiempo_entrenamiento_total': 0  # Se almacena en minutos
    }
    return f"Usuario {nombre} registrado exitosamente."

# Función para registrar ingreso y salida de un usuario ##Requisito funcional #6
def registrar_ingreso_salida(id_usuario, hora_ingreso, hora_salida):
    if id_usuario not in usuarios:
        return f"Usuario con ID {id_usuario} no encontrado."
    
    if usuarios[id_usuario]['membresia'] == 'cancelada':
        return f"La membresía del usuario {usuarios[id_usuario]['nombre']} está cancelada."
    
    # Registrar ingreso y salida
    tiempo_entrenamiento = (hora_salida - hora_ingreso).total_seconds() / 60  # Convertir a minutos
    usuarios[id_usuario]['registro_ingreso'].append({
        'hora_ingreso': hora_ingreso,
        'hora_salida': hora_salida,
        'tiempo_entrenamiento': tiempo_entrenamiento
    })
    
    # Actualizar tiempo total de entrenamiento
    usuarios[id_usuario]['tiempo_entrenamiento_total'] += tiempo_entrenamiento
    
    return f"Ingreso y salida registrados para el usuario {usuarios[id_usuario]['nombre']}. Tiempo entrenado: {tiempo_entrenamiento:.2f} minutos."

# Función para cancelar una membresía de un usuario ##Requisito funcional #8
def cancelar_membresia(id_usuario, motivo):
    if id_usuario not in usuarios:
        return f"Usuario con ID {id_usuario} no encontrado."
    
    if usuarios[id_usuario]['membresia'] == 'cancelada':
        return f"La membresía del usuario {usuarios[id_usuario]['nombre']} ya está cancelada."
    
    usuarios[id_usuario]['membresia'] = 'cancelada'
    return f"Membresía del usuario {usuarios[id_usuario]['nombre']} cancelada. Motivo: {motivo}"

# Función para activar la membresía de un usuario ##Requisito funcional #4
def activar_membresia(id_usuario):
    if id_usuario not in usuarios:
        return f"Usuario con ID {id_usuario} no encontrado."
    
    if usuarios[id_usuario]['membresia'] == 'activa':
        return f"La membresía del usuario {usuarios[id_usuario]['nombre']} ya está activa."
    
    usuarios[id_usuario]['membresia'] = 'activa'
    return f"Membresía del usuario {usuarios[id_usuario]['nombre']} ha sido activada."

# Función para eliminar un usuario
def eliminar_usuario(id_usuario):
    if id_usuario not in usuarios:
        return f"Usuario con ID {id_usuario} no encontrado."
    
    nombre_usuario = usuarios[id_usuario]['nombre']
    del usuarios[id_usuario]  # Eliminar el usuario del diccionario
    return f"Usuario {nombre_usuario} eliminado exitosamente."

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Registrar un nuevo usuario")
    print("2. Registrar ingreso y salida")
    print("3. Cancelar membresía")
    print("4. Activar membresía")
    print("5. Eliminar usuario")
    print("6. Salir")

# Función para validar entrada numérica
def solicitar_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Por favor, ingrese un número válido.")

# Función para validar el teléfono
def solicitar_telefono(mensaje):
    while True:
        telefono = input(mensaje)
        if telefono.isdigit():
            return telefono
        else:
            print("Por favor, ingrese un número de teléfono válido, solo dígitos.")

# Función principal para ejecutar el menú
def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Registrar nuevo usuario
            id_usuario = solicitar_numero("Ingrese ID del usuario: ")
            nombre = input("Ingrese nombre del usuario: ")
            correo = input("Ingrese correo del usuario: ")
            direccion = input("Ingrese dirección del usuario: ")
            telefono = solicitar_telefono("Ingrese teléfono del usuario: ")
            print(registrar_usuario(id_usuario, nombre, correo, direccion, telefono))
        
        elif opcion == '2':
            # Registrar ingreso y salida
            id_usuario = solicitar_numero("Ingrese ID del usuario: ")
            hora_ingreso = input("Ingrese hora de ingreso (HH:MM): ")
            hora_salida = input("Ingrese hora de salida (HH:MM): ")
            try:
                hora_ingreso = datetime.datetime.strptime(hora_ingreso, "%H:%M")
                hora_salida = datetime.datetime.strptime(hora_salida, "%H:%M")
                print(registrar_ingreso_salida(id_usuario, hora_ingreso, hora_salida))
            except ValueError:
                print("Formato de hora inválido. Use el formato HH:MM.")
        
        elif opcion == '3':
            # Cancelar membresía
            id_usuario = solicitar_numero("Ingrese ID del usuario: ")
            motivo = input("Ingrese el motivo de la cancelación: ")
            print(cancelar_membresia(id_usuario, motivo))
        
        elif opcion == '4':
            # Activar membresía
            id_usuario = solicitar_numero("Ingrese ID del usuario: ")
            print(activar_membresia(id_usuario))
        
        elif opcion == '5':
            # Eliminar usuario ##Se añadio esta funcionalidad como extra (por capricho)
            id_usuario = solicitar_numero("Ingrese ID del usuario: ")
            print(eliminar_usuario(id_usuario))
        
        elif opcion == '6':
            # Salir del programa
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    ejecutar_menu()
