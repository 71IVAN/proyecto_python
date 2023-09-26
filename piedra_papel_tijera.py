import random

# Inicializando diccionario para llevar un registro de las partidas
registro_de_partidas = {"jugador_uno": 0, "jugador_dos": 0, "empates": 0}

# Función para que el usuario ingrese la cantidad de partidas
def cantidad_partidas():
    while True:
        print(" ----- Bienvenido al juego de piedra papel o tijera ----- ")
        cantidad_de_juegos = int(input("Ingresa la cantidad de partidas que desea realizar: "))
        try:
            if cantidad_de_juegos <= 0:
                print("Por favor ingrese un número mayor a cero. ")
            else:
                return cantidad_de_juegos
        except ValueError:
            print("Por favor ingresar un número válido.")

# Función principal para jugar el juego
def jugar(registro_de_partidas):
    opciones = ['','piedra', 'papel', 'tijera']
    print("\n")
    jugador_uno = int(input("Escoge una opción: 1. para PIEDRA, 2. para PAPEL y 3 para TIJERA: \n "))
    print("\n")
    jugador_dos = random.randint(1, 3)  # Genera la elección aleatoria para el jugador 2

    opcion_jugador_uno = opciones[jugador_uno]
    opcion_jugador_dos = opciones[jugador_dos]

    print(f'Jugador 1 eligió: {opcion_jugador_uno}')
    print(f'Jugador 2 eligió: {opcion_jugador_dos}')
    print("\n")

    # Verificar el resultado del juego
    if jugador_uno == jugador_dos:
        print(f'¡Empate! Ambos eligieron {opcion_jugador_uno}')
        registro_de_partidas["empates"] += 1
    elif ganador(jugador_uno, jugador_dos):
        print(f'¡Gano jugador 1! Elegiste: {opcion_jugador_uno}, y jugador 2 eligió: {opcion_jugador_dos}')
        registro_de_partidas["jugador_uno"] += 1
    else:
        print(f'¡Gano jugador 2! Elegio: {opcion_jugador_dos}, y jugador 1 eligió: {opcion_jugador_uno}')
        registro_de_partidas["jugador_dos"] += 1

# Función para determinar al ganador según la lógica del juego
def ganador(jugador_principal, jugador_secundario):
    # Logica de victoria
    return (
        (jugador_principal == 1 and jugador_secundario == 3)
        or (jugador_principal == 3 and jugador_secundario == 2)
        or (jugador_principal == 2 and jugador_secundario == 1)
    )

# Solicitar al usuario la cantidad de partidas
cantidad_juegos = cantidad_partidas()

# Jugar la cantidad de partidas especificada
for _ in range(cantidad_juegos):
   jugar(registro_de_partidas)

print("\n") 

# Mostrar el registro de victorias y empates
print("Registro de victorias:")
print(f"Jugador principal: {registro_de_partidas['jugador_uno']} victorias")
print(f"Jugador secundario: {registro_de_partidas['jugador_dos']} victorias")
print(f"Empates: {registro_de_partidas['empates']} empates \n")

# Determinar al ganador global
if registro_de_partidas["jugador_uno"] > registro_de_partidas["jugador_dos"]:
    print("--Jugador uno, ha sido el ganador--")
elif registro_de_partidas["jugador_uno"] < registro_de_partidas["jugador_dos"]:
    print("--Jugador dos, ha sido el ganador--")
else:
    print("--Ambos han empatado--")

#Fin