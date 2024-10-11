my_list = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]

# Your code here
inicial_value = len(my_list)//2 #esto = a la longitud (en número) entre 2
#esto está mal inicial_value = leng(my_list/2)
stop_value = len(my_list) #como queremos imprimir del 7 en adelante, le digo que imprima toda la longitud
#Al darle como stop value = valor donde terminar, la longitud completa, le decimos que imprima desde la mitad
#Esto está mal = stop_value = (len(my_list[-1])). Porque le estoy diciendo que llegue hasta el corchete
increase_value = 1

for i in range(inicial_value, stop_value, increase_value):
    print(my_list[i])


