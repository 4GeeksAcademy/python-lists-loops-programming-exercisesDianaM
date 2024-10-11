#CORRECTO Y PASA EL TEST!!!
# 
# #Codigo original:

my_list = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]

def my_function(numbers):
    new_list = []
    for i in numbers:
        if i == 1:
            new_list.append(i)
        elif i == 0:
            new_list.append("Yahoo")
        # The magic happens here
        
        
    return new_list
    
print(my_function(my_list))


#todo lo previo:



#Busco solución para insertar elementos en lista vacía:

mi_lista = []

for num in range(3, 15, 2):
  mi_lista.append(num)


#Mi primer intento fallido da error: File "/workspaces/python-lists-loops-programming-exercisesdianamonroe2/exercises/06.1-Everything_is_awesome/app.py", line 11
    #return new_list
   # ^
#IndentationError: expected an indented block after 'for' statement on line 7


def my_function(numbers):
    new_list = []
    for i in numbers:
        if i == 1:
            new_list.append(i)
        if i == 0:
            new_list.insert("Yahoo")
        # The magic happens here

    return new_list
    
print(my_function(my_list))


def my_function(numbers):
    new_list = []
    for i in numbers:
        if i == 1:
            new_list.insert[i]
        if i == 0:
            new_list.insert("Yahoo")
        # The magic happens here

    return new_list
    
print(my_function(my_list))

#otra opción que da error TypeError: 'builtin_function_or_method' object is not subscriptable

Diana Moret, [7/9/24 17:22]
#Busco solución para insertar elementos en lista vacía:  https://www.freecodecamp.org/espanol/news/python-tutorial-de-lista-vacia-como-crear-y-comprobar-una-lista-vacia-en-python/

mi_lista = []

for num in range(3, 15, 2):
  mi_lista.append(num)


#Mi primer intento fallido da error: File "/workspaces/python-lists-loops-programming-exercisesdianamonroe2/exercises/06.1-Everything_is_awesome/app.py", line 11
    #return new_list
   # ^
#IndentationError: expected an indented block after 'for' statement on line 7


def my_function(numbers):
    new_list = []
    for i in numbers:
        if i == 1:
            new_list.append(i)
        if i == 0:
            new_list.insert("Yahoo")
        # The magic happens here

    return new_list
    
print(my_function(my_list))


def my_function(numbers):
    new_list = []
    for i in numbers:
        if i == 1:
            new_list.insert[i]
        if i == 0:
            new_list.insert("Yahoo")
        # The magic happens here

    return new_list
    
print(my_function(my_list))

#otra opción que da error TypeError: 'builtin_function_or_method' object is not subscriptable
