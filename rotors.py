import string

ALPH = string.ascii_uppercase #Constante del alfabeto
AMOUNT_LETTERS = 26 #Constante de cantidad de letras del alfabeto

#Transcribir el rotor
def read_rotor(rotor_file):
    try:
        with open(rotor_file, "r") as file:
            
            #Leer las lineas del rotor (obtendremos espacios y /n)
            lines_raw = file.readlines()

            #Lista de las lineas que queremos (ABCDE, notch)
            lines = []

            for ln in lines_raw:
                #Eliminar espacios y \n
                stripped = ln.strip()

                #Añadir solo si hay contenido (SIN LINEAS VACÍAS)
                if stripped:
                    clean_line = stripped.upper()
                    lines.append(clean_line)

        #Abecedario desordenado y notch
        wiring = lines[0]
        
        #Definir Z = notch si no hay uno predefinido
        if len(lines) > 1:
            notch = lines[1]
        else:
            notch = "Z"

        #Validar notch y wiring
        if len(wiring) != AMOUNT_LETTERS or set(wiring) != set(ALPH):
            print(f"[ERROR] {rotor_file}: Abecedario inválido")
            return None
        
        return wiring, notch
    
    except FileNotFoundError:
        print(f"[ERROR] No se ha encontrado el archivo {rotor_file}")
        return None
         
#Invertir el wiring para poder desencriptarlo más tarde
def invert_wiring(wiring):
    #Inicialización de la lista invertida
    inv = ["*"]*26

    #Iterar sobre el wiring
    for i, ch in enumerate(wiring):
        #Calcular el índice del caracter
        index = ALPH.index(ch)
        
        #Sustituir en la lista invertida
        inv[index] = ALPH[i]
    
    return "".join(inv)

#Cargar el rotor y guardar los elementos en un diccionario
def rotor_load(wiring, notch="Z", pos="A"):
    return{
        "wiring": wiring,
        "inverted": invert_wiring(wiring),
        "notch": notch,
        "position": ALPH.index(pos)
    }

#Avanzar rotor
def avanzar_rotors(rotor_1, rotor_2, rotor_3):
    #Rotor 1 siempre rota (%26 para que no se salga del array --> residuos 0 - 25)
    rotor_1["position"] = (rotor_1["position"] + 1) % AMOUNT_LETTERS

    #Calcular indice del notch en el APLH
    idx_notch_rotor_1 = ALPH.index(rotor_1["notch"])

    #Rotar el rotor 2 
    if rotor_1["position"] == idx_notch_rotor_1:
        rotor_2["position"] = (rotor_2["position"] + 1) % AMOUNT_LETTERS

        #Calcular indice del notch en el ALPH
        idx_notch_rotor_2 = ALPH.index(rotor_2["notch"])

        #Comprobar si en esta rotación coincide el notch
        if rotor_2["position"] == idx_notch_rotor_2:
            rotor_3["position"] = (rotor_3["position"] + 1) % AMOUNT_LETTERS

#Reseteo de los rotores
def reset_rotors(wiring_1, notch_1, wiring_2, notch_2, wiring_3, notch_3, posiciones):
    rotor_1 = rotor_load(wiring_1, notch_1, posiciones[0])
    rotor_2 = rotor_load(wiring_2, notch_2, posiciones[1])
    rotor_3 = rotor_load(wiring_3, notch_3, posiciones[2])
    return rotor_1, rotor_2, rotor_3