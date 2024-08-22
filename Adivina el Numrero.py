import random
def adivina_el_numero():
    numero_a_adivinar= random.randint(1,100)
    cantidad_intentos= 0
    adivinado= False
    
    print('Bienvenido  al juego')
    print('el juego consiste en adivinar  un numero aleatorio entre 1 y 100')
    print(' demuestra  que tan inteligente  eres')
    
    while not adivinado:
        adivinanza= input("introduzca un numero del  1  al 100: ")
        if adivinanza.isdigit():
            adivinanza= int(adivinanza)
            cantidad_intentos += 1
            
            if adivinanza < numero_a_adivinar :
                print(f" el numero  es mayor a {adivinanza}")
                
            elif adivinanza > numero_a_adivinar:
                print(f' el numero es menor a {adivinanza}')
            else:
                print(f' congrat  el numero es {adivinanza} y  lo lograste en {cantidad_intentos} intentos')
                
        else:
            print(' introduce un numero valido no se aceptan decimales ni texto')
            
adivina_el_numero()