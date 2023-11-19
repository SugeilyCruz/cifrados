import random
import time

#CIFRADO CESAR
def cifraCesar(cad, llave):
    cad = cad.lower()
    cifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.index(c)
            pos2 = (pos+llave)%26
            cifrado = cifrado + alfabeto[pos2]
        else:
            cifrado = cifrado + c            
    return cifrado

def descifraCesar(cad, llave):
    cad = cad.lower()
    cifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.index(c)
            pos2 = (pos-llave)%26
            cifrado = cifrado + alfabeto[pos2]
        else:
            cifrado = cifrado + c            
    return cifrado

#CIFRADO SUSTITUCION
def cifraSustituye (cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cad = cad.lower()
    cifrado = ""
    for c in cad:
        if (c in alfabeto):
            pos=alfabeto.index(c)
            cifrado=cifrado+llave[pos]
        else:
            cifrado=cifrado+c            
    return cifrado

def descifraSustituye (cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cad = cad.lower()
    texto = ""
    for c in cad:
        if (c in alfabeto):
            pos=llave.index(c)
            texto=texto+alfabeto[pos]
        else:
            texto=texto+c            
    return texto

def creaLlaveAleatoria():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cad =""
    while (len(cad)<len(alfabeto)):
        ale = random.randint(0, len(alfabeto)-1)
        c=alfabeto[ale]
        if not (c in cad):
            cad = cad+c
    return cad

 #CIFRADO Vigenère
abc = "abcdefghijklmnopqrstuvwxyz "
def cifrarVigenere(cad, clave):
    cadena = cad.lower()
    text_cifrar = ""
    i = 0
    for letra in cadena: 
        suma = abc.find(letra) + abc.find(clave[i % len(clave)])
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc[modulo]) 
        i = i + 1
    return text_cifrar
 
def descifrarVigenere(cad, clave):  
    cadena = cad.lower()
    text_cifrar = ""
    i = 0
    for letra in cadena:
        suma = abc.find(letra) - abc.find(clave[i % len(clave)])  
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc[modulo])  
        i = i + 1
    return text_cifrar

# Función principal para seleccionar el tipo de cifrado
def main():
    while True:
        print("Seleccione el tipo de cifrado:")
        print("1. Cifrado Cesar")
        print("2. Cifrado de Sustitucion")
        print("3. Cifrado Vigenere")
        print("\nSeleccione el tipo de descifrado:")
        print("4. desCifrado Cesar")
        print("5. desCifrado de Sustitucion")
        print("6. desCifrado Vigenere")
        print("\n7. Salir\n")

        opcion = int(input("Ingrese el numero correspondiente al tipo de cifrado: "))

        if opcion == 1:
            texto = input("Ingrese el texto a cifrar: ")
            desplazamiento = int(input("Por favor, ingrese un numero para el desplazamiento en el cifrado Cesar: "))
            texto_cifrado = cifraCesar(texto, desplazamiento)
            print("Texto final:", texto_cifrado, "\n")
            
            time.sleep(1) 
        elif opcion == 2:
            texto = input("Ingrese el texto a cifrar: ")
            print("Si desea que la llave sea generada por el programa coloque la palabra 'default' ")
            llave = input("Por favor, ingrese una llave para el cifrado por sustitución: ")
            if llave == "default":
                llave = creaLlaveAleatoria()
                print(f"Su llave para el cifrado por sustitución es: {llave}")
            texto_cifrado = cifraSustituye(texto, llave)
            print("Texto final:", texto_cifrado, "\n")
            time.sleep(1)  
        elif opcion == 3:
            texto = input("Ingrese el texto a cifrar: ")
            clave = input("Por favor, ingrese una clave para el cifrado Vigenère: ")
            texto_cifrado = cifrarVigenere(texto, clave)
            print("Texto final:", texto_cifrado, "\n")
            time.sleep(1)  
        elif opcion == 4:
            texto = input("Ingrese el texto a descifrar: ")
            desplazamiento = int(input("Por favor, ingrese un numero para el desplazamiento en el cifrado Cesar: "))
            texto_cifrado = descifraCesar(texto, desplazamiento)
            print("Texto final:", texto_cifrado, "\n")
            time.sleep(1) 
        elif opcion == 5:
            texto = input("Ingrese el texto a descifrar: ")
            llave = input("Por favor, ingrese una llave para el descifrado por sustitución: ")
            texto_cifrado = descifraSustituye(texto, llave)
            print("Texto final:", texto_cifrado, "\n")
            time.sleep(1)  
        elif opcion == 6:
            texto = input("Ingrese el texto a descifrar: ")
            clave = input("Por favor, ingrese una clave para el descifrado Vigenère: ")
            texto_cifrado = descifrarVigenere(texto, clave)
            print("Texto final:", texto_cifrado, "\n")
            time.sleep(1)  
        elif opcion == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 7.")

# Llamada a la función principal
if __name__ == "__main__":
    main()