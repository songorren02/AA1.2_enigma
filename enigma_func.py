import re


texto_prueba = "Hola, qUe! tal. estas?"

#Estandarizar el formato de texto
def normalizar_texto(texto):

    #Quitamos mayusculas, espacios y caracteres especiales
    texto = texto.upper()
    texto = texto.replace(" ", "")
    texto = re.sub(r'[^\w]', '', texto) 

    contador = 0
    texto_new = ""

    #Añadimos espacios nuevos cada 5 caracteres
    for ch in texto:
        if contador != 0 and contador % 5 == 0:
            texto_new = texto_new + " "
        texto_new = texto_new + ch
        contador += 1

    return texto_new

normalizar_texto(texto_prueba)