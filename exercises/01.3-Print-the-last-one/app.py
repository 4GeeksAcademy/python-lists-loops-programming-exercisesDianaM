#CÓDIGO ORIGINAL

# import the random package here "import random"
import random

aux_list = []

def generate_random_list():
    randomlength = random.randint(1, 100) #Esto genera una lista de números random del 1 al 99
    for i in range(randomlength): #Esto hace un bucle con una variable "i" con todos los valores de randomlength (es un rango del 1 al 99)
        aux_list.append(randomlength) #Append lo lleva a la última por defecto (mientras .insert le tengo que indicar ne que posición)
        i = i+2
    return aux_list #El return No lo puedo quitar!!! La función se encarga de hacer algo y el return devuelve esos cambios al print que hay que hacer



print(generate_random_list())
# Write your code below this comment, good luck!





