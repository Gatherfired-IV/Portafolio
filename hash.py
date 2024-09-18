import hashlib

hash_file= "#########################"

dic_file=input("Ingrese la direccion del archivo de diccionario: ")

with open(dic_file,'r') as file:

    diccionario=[line.strip for line in file]

    for pasword in diccionario:

        hash_calculado = hashlib.sha256(pasword.encode()).hexdigest()

        if hash_calculado == hash_file:

            print("La contraseña original es: "+ pasword)
            break
        else:
            print("La contraseña no se encuentra en el diccionario ")