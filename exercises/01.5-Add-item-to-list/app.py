# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

#NO FUNCIONA!!!
# añadir 10 elementos a una lista:  my_list += 10
for i in range(10):
    #tiene que ser range(10) no range(11) si no me llena la lista random com 11 índices en lugar de 10 y no pasa el test
    my_list.append(random.randint(1,10))
    #ME Faltaba print!!!!!
    #El print se lo digo a la consola
    #El return es para un bucle para el que necesitamos trabajar mas adelante con el resultado, ahora no necesito un return
    print(i)

print(my_list)

#todo lo anteriormente probado y explicación opciones:
