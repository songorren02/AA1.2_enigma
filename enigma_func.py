import re
import string
import rotors as r

ALPH = string.ascii_uppercase #Constante del alfabeto
AMOUNT_LETTERS = 26 #Constante de cantidad de letras del alfabeto

texto_prueba = "Hola, qUe! tal. estas?"

#Estandarizar el formato de texto
def normalizar_texto(texto):
    #Quitamos mayusculas, espacios y caracteres especiales
    texto = texto.upper()
    texto = texto.replace(" ", "")
    texto = re.sub(r'[^A-Z]', '', texto) 

    return texto

#Función añadir espacios
def espacios(texto):
    texto_new = ""
    contador = 0

    #Añadimos espacios nuevos cada 5 caracteres
    for ch in texto:
        if contador != 0 and contador % 5 == 0:
            texto_new = texto_new + " "
        texto_new = texto_new + ch
        contador += 1

    return texto_new

#Pasar las letras por los rotores para encriptar luego
def input_rotor_encrypt(rotor, letra):
    #Obtener la posicion de la letra 
    letra_idx = ALPH.index(letra)

    #Sumamos la rotación
    input = (letra_idx + rotor["position"]) % AMOUNT_LETTERS
    
    #Encriptamos la letra
    cripted = rotor["wiring"][input]

    #Obtenemos la posción equivalente a la letra
    cripted_idx = ALPH.index(cripted)

    #Quitamos la rotación para obtener el indice real
    output = (cripted_idx - rotor["position"]) % 26

    return ALPH[output]


#Pasar las letras por los rotores para encriptar luego
def input_rotor_decrypt(rotor, letra):
    #Obtener la posicion de la letra 
    letra_idx = ALPH.index(letra)

    #Sumamos la rotación
    input = (letra_idx + rotor["position"]) % AMOUNT_LETTERS
    
    #Encriptamos la letra
    cripted = rotor["inverted"][input]

    #Obtenemos la posción equivalente a la letra
    cripted_idx = ALPH.index(cripted)

    #Quitamos la rotación para obtener el indice real
    output = (cripted_idx - rotor["position"]) % 26

    return ALPH[output]


#Cifrar el mensaje
def encrypt(texto, rotor_1, rotor_2, rotor_3):
    output = ""

    #Recorremos el mensaje
    for ch in texto:
        #Avanzamos/comprovamos notchs
        r.avanzar_rotors(rotor_1, rotor_2, rotor_3)
        
        #Le pasamos la letra a los rotores
        ch = input_rotor_encrypt(rotor_1, ch)
        ch = input_rotor_encrypt(rotor_2, ch)
        ch = input_rotor_encrypt(rotor_3, ch)

        #Concatenamos en output
        output += ch
    
    return output

#Descrifrar mensaje
def decrypt(texto, rotor_1, rotor_2, rotor_3):
    output = ""

    #Recorremos el mensaje
    for ch in texto:
        #Avanzamos/comprovamos notchs
        r.avanzar_rotors(rotor_1, rotor_2, rotor_3)
        
        #Le pasamos la letra a los rotores
        ch = input_rotor_decrypt(rotor_3, ch)
        ch = input_rotor_decrypt(rotor_2, ch)
        ch = input_rotor_decrypt(rotor_1, ch)

        #Concatenamos en output
        output += ch
    
    return output

#Abrir el archivo del mensaje
def open_msg(file_name):
    try:
        with open(file_name, "r",) as file:
            #Leer msg
            msg = file.read()

        #Normalizar msg
        msg_normalized = normalizar_texto(msg)
        return msg_normalized
    
    except FileNotFoundError:
        print(f"[ERROR] No se encuentra el archivo {file_name}")
    return None

#Guardar el mensaje en archivo
def save_msg(texto, file_name):
    with open(file_name, "w") as file:
        file.write(texto)

def edit_rotor():
    try:
        rotor_num = int(input("Qué rotor quieres editar? (1, 2 o 3) "))
    except ValueError:
        print("[ERROR] Debes introducir un número válido")
        return None

    #Verificar si el input es válido
    if rotor_num not in [1, 2, 3]:
        print("[ERROR] Solo puedes elegir 1, 2 o 3")
        return None

    #Pedir nuevo wiring y notch
    new_wiring = input("Introduce el nuevo wiring (26 letras A-Z sin repetir): ").upper()
    new_notch = input("Introduce el nuevo notch (una letra A-Z): ").upper()

    #Validar wiring
    if len(new_wiring) != AMOUNT_LETTERS or set(new_wiring) != set(ALPH):
        print(f"[ERROR] Abecedario inválido")
        return None   

    #Validar notch
    if new_notch not in ALPH:
        print("[ERROR] Notch inválido")
        return None

    #Guardar los cambios en los archivos
    file_name = f"rotors/rotor{rotor_num}.txt"

    #Abrir y escribir (Sobreescribir)
    with open(file_name, "w", encoding="utf-8") as rotor_file:
        #Escribir el wiring
        rotor_file.write(new_wiring + "\n")
        #Escribir el notch
        rotor_file.write(new_notch + "\n")
  
    return rotor_num