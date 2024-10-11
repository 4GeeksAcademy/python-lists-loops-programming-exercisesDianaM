my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

aux_var = []

#Solución 

def sum_odds():
    suma = 0 #Esto está fuera del for para que no parta de cero dentro del loop, porque al final el lopp
    for a in my_list:
      if a % 2 != 0: 
         suma += a #Esto signficia total + num (o suma = suma + a, es una alternativa de sum() que me lo suma todo, en cambio += me suma solo que queremos), pero se abrevia. A total le suma lo que tengo a la derecha
         # si es -n, lo que tengo a la izquierda le resto lo que tengo a la derecha. 
         #Le sumamos la variable a a la variable suma, sumar solo los impares. Esto me previene crear una función previa para crear lista de impares antes y usar sum()
         
    return suma

print(sum_odds()) 

#La solución fue cogida de aquí  https://beastieux.com/2011/03/16/codigo-python-suma-de-elementos-impares-de-una-lista/

def sumar_impares_lista(lista):
    suma = 0
    for num in lista:
        if num % 2 != 0:
            suma += num
 
    return suma


#Opcion 1)
def sum_odds():
   for a in my_list:
       if a % 2 != 0:
           aux_var.append(a)
           print(sum(aux_var))
        

print(sum_odds())


#Opcion 2)
def sum_odds():
   for a in my_list:
       if a % 2 != 0:
        aux_var.append(a)
        print(aux_var)
        
sum_odds()

#OUTPUT:
[5]
[5, 43]
[5, 43, 45]
[5, 43, 45, 23]
[5, 43, 45, 23, 67]
[5, 43, 45, 23, 67, 23]
[5, 43, 45, 23, 67, 23, 45]



#Opcion 3)
def sum_odds():
   for a in my_list:
       if a % 2 != 0:
        aux_var.append(sum(my_list))
        return aux_var
        
print(sum_odds())

#Output: 
[1207]

#Pasos previos: Identiticar los números primos:

#Opción 1)

def sum_odds():
    for a in my_list:
        if a % 2 != 0:
          print(f"El número {a} es impar")

sum_odds()

#Opción 2)


def sum_odds():
    for a in my_list:
        if a % 2 != 0:
            print(a, "is Impar")

sum_odds()

def sum_odds():
   for a in my_list:
       if a % 2 != 0:
           total = sum(my_list)
           return total


print(sum_odds())



#NO FUNCIONA
def sum_odds():
   for a in my_list:
       if a % 2 != 0:
           print(a)
           total = sum(my_list)
           return total


print(sum_odds())




# Your code here




#pasos previos:


def sum_odds():
   for a in my_list:
       if a % 2 != 0:
           print(a, "is Impar")


sum_odds()


# Your code here


#Otra forma que da el outpu correcto

def odds():
    odds = []
    for pepito in my_list:
       if pepito % 2 != 0:
           odds.append(pepito)
    return odds
print(odds())

print(sum(odds()))
