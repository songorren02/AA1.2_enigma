import enigma_func as f
import rotors as r
import time

NUM_ROTORES = 3
MSG_FILE = "mensaje.txt"
ENCRYPTED_FILE = "output/cifrado.txt"
DECRYPTED_FILE = "output/mensaje_desencriptado.txt"

#Variable de control while
close_enigma = False

#Leer rotores desde los archivos
wiring_1, notch_1 = r.read_rotor("rotors/rotor1.txt")
wiring_2, notch_2 = r.read_rotor("rotors/rotor2.txt")
wiring_3, notch_3 = r.read_rotor("rotors/rotor3.txt")

#Pedimos al usuario la posición en la que quiere que empiecen los rotores
def position():
    print("En qué posición quieres que empiecen los rotores? ")
    
    #Inicialización de la lista de la posición inicial
    rotores = ["*"] * NUM_ROTORES

    #Preguntar la posición
    for i in range(NUM_ROTORES):
        mensaje = input(f"Posición inicial del rotor {i+1}: ").upper()
        if mensaje in f.ALPH:
            rotores[i] = mensaje
        else:
            print("[ERROR] Letra no aceptada, se utilizará A por defecto")
            rotores[i] = "A"
    
    #Mostrar la config
    print("[CONFIG] Configurando rotores...")
    time.sleep(1)

    print(f"[CONFIG] Tu configuración de los rotores es: {rotores}\n")
    
    return rotores

#Pedir mensaje
def msg_to_encrypt():
    print()

#Creamos el menú
def print_menu():
    print("             ENIGMA")
    print("-------------------------------")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Editar rotores")
    print("4. Salir")
 
#Elegir opcion
def choose_menu(wiring_1, notch_1, wiring_2, notch_2, wiring_3, notch_3, posiciones):
    #Validación del input
    try:
        opt = int(input("¿Qué opción quieres hacer? "))
    except ValueError:
        print("[ERROR] Debes introducir un número")
        return None

    if opt == 1: #Cifrar
        #Reset de los rotores
        rotor_1, rotor_2, rotor_3 = r.reset_rotors(wiring_1, notch_1, wiring_2, notch_2, wiring_3, notch_3, posiciones)

        #Abrir archivo
        msg = f.open_msg(MSG_FILE)
        
        #Encriptar el texto
        texto_encrypted = f.encrypt(msg, rotor_1, rotor_2, rotor_3)

        #Añadir espacios
        texto_espaced = f.espacios(texto_encrypted)

        #Guardar en archivo
        f.save_msg(texto_espaced, ENCRYPTED_FILE)

        #Mensajes por terminal
        print("\n[ENIGMA] Cifrando mensaje...")
        time.sleep(1)
        print("[ENIGMA] Mensaje cifrado con éxito!\n")

    elif opt == 2: #Descifrar
        #Reset de los rotores
        rotor_1, rotor_2, rotor_3 = r.reset_rotors(wiring_1, notch_1, wiring_2, notch_2, wiring_3, notch_3, posiciones)

        #Abrimos con open_msg() así normalizamos texto que se pueda haber escrito a mano
        msg_encrypted = f.open_msg(ENCRYPTED_FILE)

        #Desencriptar el mensaje
        msg_decrypted = f.decrypt(msg_encrypted, rotor_1, rotor_2, rotor_3)

        #Guardamos en archivop
        f.save_msg(msg_decrypted, DECRYPTED_FILE)

        #Mensajes por terminal
        print("\n[ENIGMA] Descifrando mensaje...")
        time.sleep(1)
        print("[ENIGMA] Mensaje desencriptado con éxito!")

    elif opt == 3:
        #Funcion editar rotor
        rotor_num = f.edit_rotor()        
        
        #Miramos cual es el rotor modificado
        if rotor_num == 1:
            wiring_1, notch_1 = r.read_rotor("rotors/rotor1.txt")
        elif rotor_num == 2:
            wiring_2, notch_2 = r.read_rotor("rotors/rotor2.txt")
        elif rotor_num == 3:
            wiring_3, notch_3 = r.read_rotor("rotors/rotor3.txt")


        #Reset de los rotores
        rotor_1, rotor_2, rotor_3 = r.reset_rotors(wiring_1, notch_1, wiring_2, notch_2, wiring_3, notch_3, posiciones)

    elif opt == 4:
        close_enigma = True
        exit()

    else:
        print("[ERROR] Opción inválida")





posiciones = position()

while not close_enigma:
    print_menu()
    choose_menu(wiring_1, notch_1, wiring_2, notch_2, wiring_3, notch_3, posiciones)
