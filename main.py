import enigma_func as f
import rotors as r
NUM_ROTORES = 3


#Leer rotores desde los archivos
wiring_1, notch_1 = r.read_rotor("rotors/rotor1.txt")
wiring_2, notch_2 = r.read_rotor("rotors/rotor2.txt")
wiring_3, notch_3 = r.read_rotor("rotors/rotor3.txt")

#Pedimos al usuario la posición en la que quiere que empiecen los rotores
def position():
    print("En qué posición quieres que empiecen los rotores? ")
    rotores = ["*"] * NUM_ROTORES
    for i in range(NUM_ROTORES):
        mensaje = input(f"Posición inicial del rotor {i+1}: ")
        if mensaje in f.ALPH:
            rotores[i] = mensaje
        else:
            print("[ERROR] Letra no aceptada, se utilizará A por defecto")
            rotores[i] = "A"
    
    return rotores

posiciones = position()

#Cargamos cada rotor individualmente
rotor_1 = r.rotor_load(wiring_1, notch_1, posiciones[0])
rotor_2 = r.rotor_load(wiring_2, notch_2, posiciones[1])
rotor_3 = r.rotor_load(wiring_3, notch_3, posiciones[2])
        

#Creamos el menú
def print_menu():
    print("             ENIGMA")
    print("-------------------------------")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Editar rotores")
    print("4. Salir")

 
print_menu()

def choose_menu(rotor_1, rotor_2, rotor_3):
    opt = int(input("¿Qué opción quieres hacer? "))

    if opt == 1:
        texto = input("Introduce el texto a cifrar: ")
        texto = f.normalizar_texto(texto)
        print(f.encrypt(texto, rotor_1, rotor_2, rotor_3))
    elif opt == 2:
        texto = input("Introduce el texto a cifrar: ")
        texto = f.normalizar_texto(texto)
        print(f.decrypt(texto, rotor_1, rotor_2, rotor_3))

    elif opt == 3:
        #Funcion editar rotor
        print("Editar rotor")
    elif opt == 4:
        exit()
    else:
        print("[ERROR] Opción inválida")

choose_menu(rotor_1, rotor_2, rotor_3)
