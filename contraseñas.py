import string
import random

longitud = int(input("Ingrese el tamaño de la contraseña: "))

carecteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(carecteres) for i in range(longitud))

print ("La contraseña generada es: " + contraseña)


