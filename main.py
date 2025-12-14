import enigma_func as f
import rotors as r


#Leer rotores desde los archivos
wiring_1, notch_1 = f.read_rotor("rotor1.txt")
wiring_2, notch_2 = f.read_rotor("rotor2.txt")
wiring_3, notch_3 = f.read_rotor("rotor3.txt")
     

#Creamos el menú
def print_menu():
    print("             ENIGMA")
    print("-------------------------------")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Editar rotores")
    print("4. Salir")


print_menu()

def choose_menu():
    opt = int(input("¿Qué opción quieres hacer? "))
    print(opt)

    if opt == 1:
        f.encrypt()
    elif opt == 2:
        f.decrypt()
    elif opt == 3:
        #Funcion editar rotor
        print("Editar rotor")
    elif opt == 4:
        exit()
    else:
        print("[ERROR] Opción inválida")

choose_menu()
