import string

#Constante del alfabeto
ALPH = string.ascii_uppercase

def read_rotor(rotor_file):
    try:
        with open(rotor_file, "r") as file:
            
            #Leer las lineas del rotor (obtendremos espacios y mierdas)
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
        notch = lines[1] if len(lines) > 1 else "Z" 

        #Validar notch y wiring
        if len(wiring) != 26 or set(wiring) != set(ALPH):
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

wiring, notch = read_rotor("rotors/rotor1.txt")
print(wiring, notch)

print(invert_wiring(wiring))