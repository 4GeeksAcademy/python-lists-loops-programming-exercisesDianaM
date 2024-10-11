mixed_list = ['1','5','45','34','343','34',6556,323]

def type_list(mixed_list):
        # Your code here
         return type(mixed_list)

new_list = list(map(type_list, mixed_list))

print(new_list)

#output correcto pero no pasa el test:

def type_list(items):
        for items in mixed_list: #Otra vez, la función map() no necesita que le especifiquemos con For elemento in list que pase la función por cada elemento
        # Your code here
         return type(items)

new_list = list(map(type_list, mixed_list))

print(new_list)
