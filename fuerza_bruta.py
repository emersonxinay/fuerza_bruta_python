import itertools
import string
import getpass

# password_objetivo = "@bDa"  # password que queremos encontrar
def probar_password(password):
    return password == password_objetivo

def buscar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    combinaciones = itertools.product(caracteres, repeat=longitud)
    contador = 0
    for combinacion in combinaciones:
        contador += 1
        password = ''.join(combinacion)
        print(f"combinación {contador} : {password}  ")
        if probar_password(password):
            print("password encontrada:", password)
            print(f"Numero de combinaciones:{contador}")
            return True
    print(f"No se encontró ninguna coincidencia con {longitud} caracteres, posiblemente tenga mas caracteres.")
    print(f"Numero de combinaciones:{contador}")
    return False
contra = int(input("ingrese un número para el tamaño de longitud de su password: "))
password_objetivo = getpass.getpass(f"Ingrese su password de {contra} caracteres: ")
buscar_password(contra)
