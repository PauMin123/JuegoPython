import random
import os

def menuprin(apodo):
    a = [[0] for _ in range(3)]
    while True:
        print("")
        print("***** BIENVENIDO AL JUEGO ", apodo, " ****")
        print("***** JUEGOS DE PROBLEMAS MATEMATICOS ****")
        print("1. Problemas matematicos")
        print("2. Problemas logicos")
        print("3. Adivinar una letra")
        print("4. Puntos Obtenidos")
        print("5. Salir")
        print("*******************")
        print("Elija una opcion:")
        opcion = int(input())
        if opcion == 1:
            print("Bienvenido a problemas matematicos")
            problemamatematico(apodo, a[0][0], a)
        elif opcion == 2:
            print("Problemas logicos")
            problemalogico(apodo, a[1][0], a)
        elif opcion == 3:
            print("Adivina una letra")
            adivinaunaletra(apodo, a[2][0], a)
        elif opcion == 4:
            print("")
            print("Puntos obtenidos")
            print("1. En problemas matematicos obtuviste:", a[0][0], " puntos")
            print("2. En problemas logicos obtuviste:", a[1][0], " puntos")
            print("3. En adivinar una letra obtuviste:", a[2][0], " puntos")
            print("¡", apodo, " Obtuviste un total de: ", a[0][0] + a[1][0] + a[2][0], " puntos!")
            print("presione 0 para salir")
            n = input()
        if opcion == 5:
            break

		
		
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def problemamatematico(apodo, puntosnivel, a):
	puntosnivel = 0
	# Nivel 1---------------------------------------------------------------------
	clear_screen()
	puntos = float()
	respuesta = int()
	while True:
		puntos = 0
		print("-------Problemas Matematicos-------")
		print("-------------Nivel 1-------------")
		# Pregunta 1
		print("Pregunta 1: ¿Cuánto es 2 + 2?")
		print("1) 2")
		print("2) 4")
		print("3) 5")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break #Sale del bucle si la respuesta es 0
		else:
			if respuesta==2:
				puntos = puntos+1
			else:
				print(apodo," Su respuesta es incorrecta")
		# Pregunta 2
		print("Pregunta 2: ¿Cuánto es 10 * 8?")
		print("1) 102")
		print("2) 4")
		print("3) 80")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break
		if respuesta==3:
			puntos = puntos+1
		else:
			print(apodo," Su respuesta es incorrecta")
		# Pregunta 3
		print("Pregunta 3: Juan tiene 7 manzanas y su amigo Pedro le da 3 manzanas más. ¿Cuántas manzanas tiene Juan en total?")
		print("1) 7")
		print("2) 10")
		print("3) 5")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break
		else:
			if respuesta==2:
				puntos = puntos+1
			else:
				print(apodo," Su respuesta es incorrecta")
		# Pregunta 4
		print("Pregunta 4: Un agricultor tiene un terreno rectangular que mide 20 metros de largo y 10 metros de ancho.")
		print("Quiere dividirlo en parcelas cuadradas de 5 metros de lado.")
		print("¿Cuántas parcelas podrá crear en total y cuánto terreno quedará sin utilizar?")
		print("1) 8")
		print("2) 10")
		print("3) 20")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break
		else:
			if respuesta==1:
				puntos = puntos+2
			else:
				print(apodo," Su respuesta es incorrecta")
		if puntos==5: break
	# Verificar puntos
	if puntos==5:
		print("¡Felicidades!", apodo, " Has alcanzado 5 puntos y puedes avanzar al siguiente nivel.")
		print(apodo," ¿Desea avanzar al siguiente nivel?")
		print("1. Si")
		print("2. No")
		avanzar = input()
		if avanzar==1:
			clear_screen()
			print("----Avanzaste al siguiente nivel----")
	while True:
			clear_screen()
			print("--------------Nivel 2---------------")
			print(" ")
			
			# pregunta 1 nivel 2
			print("Si tienes 2 horas y 30 minutos para estudiar matemáticas cada día,")
			print("y decides estudiar durante 1 hora y 45 minutos, ¿cuánto tiempo te queda para estudiar otros temas?")
			print("1. 30 minutos")
			print("2. 25 minutos")
			print("3. 45 minutos")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==3:
					puntos = puntos+1.5
				else:
					print(apodo," Su respuesta es incorrecta")
			# pregunta 2 nivel 2
			print("Problema de suma con fracciones y enteros:Si tienes 3/4 de pizza y luego comes 1/8 de la pizza")
			print("¿cuánto de la pizza original te queda?")
			print("1. 1/8 de la pizza original")
			print("2. 5/8 de la pizza original")
			print("3. 7/8 de la pizza original")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==2:
					puntos = puntos+1
				else:
					print(apodo," Su respuesta es incorrecta")
			# pregunta 3 nivel 2
			print("En una competencia de natación, Juan nada 1.5 kilómetros en la primera etapa y luego 2.75 kilómetros en la segunda etapa.")
			print("Si luego nadó 0.5 kilómetros más")
			print("¿cuál fue la distancia total que nadó Juan?")
			print("1. 4.75 km")
			print("2. 8 km")
			print("3. 3.75")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==1:
					puntos = puntos+1.5
				else:
					print(apodo," Su respuesta es incorrecta")
			# pregunta 4 nivel 2
			print("Resuelva: 2(5+2)^2 - 3(4-2)^3")
			print("1. 84")
			print("2. 74")
			print("3. 164")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==1:
					puntos = puntos+1
				else:
					print(apodo," Su respuesta es incorrecta")
			puntosnivel = puntos
			a[0][0] = puntosnivel
			if puntos==10:
				print("!Buen trabajo¡", apodo, " haz obtenido 10 puntos ")
			else:
				if puntos < 10:
					print(apodo, "Debes seguir practicando haz obtenido ", puntos, " puntos") 
			break

def problemalogico(apodo, puntosnivel1, a):
	# Nivel 1---------------------------------------------------------------------
	print("") 
	puntos = float()
	respuesta = int()
	while True:
		puntos = 0
		print("-------Problemas Logicos-------")
		print("-------------Nivel 1-------------")
		# Pregunta 1
		print("Pregunta 1: ¿Qué grupo continúa la siguiente serie: 2Z3, 4Y5, 6X7?...")
		print("1) 8W9")
		print("2) 8S9")
		print("3) 8U9")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break
		else:
			if respuesta==1:
				puntos = puntos+1
			else:
				print(apodo," Su respuesta es incorrecta")
		# Pregunta 2
		print("Pregunta 2: Un granjero tiene 10 conejos, 20 caballos y 40 cerdos. Si llama caballos a los cerdos, ¿Cuántos caballos tendrá realmente?")
		print("1) 40")
		print("2) 60")
		print("3) 20")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break
		else:
			if respuesta==3:
				puntos = puntos+1
			else:
				print(apodo," Su respuesta es incorrecta")
		# Pregunta 3
		print("Pregunta 3: Una madre tiene 40 años y su hijo tiene 10. ¿Cuántos años deben pasar para que la edad de la madre sea el triple que la edad de su hijo?")
		print("1) 10 años")
		print("2) 5 años")
		print("3) 15 años")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break
		else:
			if respuesta==2:
				puntos = puntos+1
			else:
				print(apodo," Su respuesta es incorrecta")
		# Pregunta 4
		print("Pregunta 4: Un niño consume 500 gramos diarios de pan.")
		print("¿Cuál será el consumo diario en kilos de un comedor compuesto por 126 niños?")
		print("1) 63 kg")
		print("2) 15 kg")
		print("3) 28 kg")
		respuesta = int(input())
		if respuesta==0:
			menuprin(apodo)
			break
		else:
			if respuesta==1:
				puntos = puntos+2
			else:
				print(apodo," Su respuesta es incorrecta")
		if puntos==5: break
	# Verificar puntos
	if puntos==5:
		print("¡Felicidades!", apodo, " Has alcanzado 5 puntos y puedes avanzar al siguiente nivel.")
		print(apodo," ¿Desea avanzar al siguiente nivel?")
		print("1. Si")
		print("2. No")
		avanzar = input()
		if avanzar==1:
			print("----Avanzaste al siguiente nivel----")
	while True: 
			clear_screen()
			print("--------------Nivel 2---------------")
			print(" ")
			# pregunta 1 nivel 2
			print("Supongamos que tienes 4 perros que alimentar: un labrador, un akita, un pitbull y un pastor alemán.")
			print("El pastor alemán come más que el labrador, el pitbull como más que el labrador y menos que el akita, pero el akita come más que el pastor alemán. ")
			print("¿Cuál de los 4 es el perro que menos come?")
			print("1. Pitbull")
			print("2. Akita")
			print("3. Labrador")
			print("4. Pastor alemán")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==3:
					puntos = puntos+1.5
				else:
					print(apodo," Su respuesta es incorrecta")
			# pregunta 2 nivel 2
			print("Cuatro personas deben cruzar un puente en la oscuridad. Solo tienen una linterna y el puente solo puede soportar el peso de dos personas a la vez.")
			print(" Cada persona cruza el puente a diferentes velocidades: uno en 1 minuto, otro en 2 minutos, otro en 5 minutos y el último en 10 minutos. Cuando dos personas cruzan juntas, caminan al ritmo del más lento.")
			print(" ¿Cuál es el tiempo mínimo necesario para que todos crucen el puente de manera segura con una sola linterna?")
			print("1. 41 minutos")
			print("2. 33 minutos")
			print("3. 18 minutos")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==2:
					puntos = puntos+1
				else:
					print(apodo," Su respuesta es incorrecta")
			# pregunta 3 nivel 2
			print("En una funda se tienen 15 fichas, numeradas del 1 al 15 se extrae una ficha y se sabe que es numero par")
			print("¿Cual es la probabilidad de que este numero sea divisible por 3?")
			print("1. 1/3")
			print("2. 2/15")
			print("3. 2/7")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==3:
					puntos = puntos+1
				else:
					print(apodo," Su respuesta es incorrecta")
			# pregunta 4 nivel 2
			print("Un hombre le dice a alguien: Tengo tres hijos. El producto de sus edades es 36 y la suma de sus edades es igual al número de tu casa")
			print("La persona piensa un momento y luego responde: No puedo decir cuál es la edad de tus hijos.")
			print("El hombre entonces le dice: Mi hijo mayor juega al ajedrez. La persona finalmente sabe cuáles son las edades de los tres hijos. ¿Cuáles son?")
			print("1. 2 años, 3 años, 4 años")
			print("2. 2 años, 2 años, 9 años")
			print("3. 1 año, 1 año, 36 años")
			respuesta = int(input())
			if respuesta==0:
				menuprin(apodo)
				break
			else:
				if respuesta==2:
					puntos = puntos+1.5
				else:
					print(apodo," Su respuesta es incorrecta")
			puntosnivel1 = puntos
			a[1][0] = puntosnivel1
			if puntos==10:
				print("!Buen trabajo¡", apodo, " haz obtenido 10 puntos ")
			else:
				if puntos < 10:
					print(apodo, "Debes seguir practicando haz obtenido ", puntos, " puntos") 
			break	


def adivinaunaletra(apodo, puntosnivel2, a):
    puntos = 0  # Inicializamos la variable puntos
    letras = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    while True:
        clear_screen()  # Limpiar la pantalla al principio del bucle
        letraaleatoria = random.choice(letras[:26])
        intentos = 5
        adivinado = False
        print("¡Bienvenido al juego de letras!")
        print("********Estás en el nivel 1*******")
        print("Tienes 5 intentos para adivinar una letra (entre minúsculas).")
        print(letraaleatoria)
        for i in range(1, 6):
            print(f"Adivina la letra aleatoria, Intento {i}:")
            adiv = input().lower()  # Convertir la entrada del usuario a minúsculas
            if adiv == "0":
                menuprin(apodo)
                break
            if adiv.lower() == letraaleatoria.lower():  # Convertir tanto la letra aleatoria como la entrada del usuario a minúsculas
                print("¡Correcto!")
                adivinado = True
                i = 5
                puntos = 5  # Actualizar la variable puntos a 5
                print("¿Quieres pasar al siguiente nivel?")
                print("1. Sí")
                print("2. No")
                opcion = input()
                if opcion == "1":
                    clear_screen()
                    print("")
                    print("********Estás en el nivel 2*******")
                    print("Tienes 5 intentos para adivinar una letra (Entre mayúsculas y minúsculas).")
                    letraaleatoria = random.choice(letras)
                    intentos = 5
                    adivinado = False
                    print(letraaleatoria)
                    for i in range(1, 6):
                        print(f"Adivina la letra aleatoria, Intento {i}:")
                        adiv = input().lower()  # Convertir la entrada del usuario a minúsculas
                        if adiv == "0":
                            menuprin(apodo)
                            break
                        if adiv.lower() == letraaleatoria.lower():  # Convertir tanto la letra aleatoria como la entrada del usuario a minúsculas
                            print("¡Correcto!", puntosnivel2)  # Mostrar puntosnivel2 aquí
                            adivinado = True
                            i = 5
                            puntosnivel2 = puntosnivel2 + 10  # Actualizar puntosnivel2
                            a[2][0] = puntosnivel2  # Agregar el puntaje a la matriz a[2]
                            menuprin(apodo)  # Llamada a menuprin
                            break
                        else:
                            intentos = intentos - 1
                            print(f"Incorrecto. Te quedan {intentos} intentos.")
                    if not adivinado:
                        print(f"No adivinaste la letra. La letra era {letraaleatoria}")
                elif opcion == "2":
                    menuprin(apodo)
                    break
            else:
                intentos = intentos - 1
                print(f"Incorrecto. Te quedan {intentos} intentos.")
        if not adivinado:
            print(f"No adivinaste la letra. La letra era {letraaleatoria}")

if __name__ == '__main__':
    apodo = input("Ingrese su Apodo: ")
    menuprin(apodo)