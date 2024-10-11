#VER DETALLE Y EXPLICACIÓN DE DISTINTAS FÓRMULAS Y ERRORES AQUÍ https://colab.research.google.com/drive/1Xp38FGaN6gaMw3bfGMZnM9l9uSwlns-0?authuser=1#scrollTo=iEqG9UlVYb_7

people = ['juan','ana','michelle','daniella','stefany','lucy','barak']
#Fuera de la función lamo a la lista como es no como quiero que sea, si la meto dentro la modifico con la función
#new_list = [] está vacía así que no sirve como .append para .remove

#Opción A) si pasa el test: usando .append() (EN LUGAR DE .remove()) + IF STATEMENT + FOR LOOP

def delete_person(person_name):
    new_list = []
    for name in people:
        if name != person_name:
            new_list.append(name) 
      #return new_list #Ojo: si idento el return al mismo nivel que new_list.append, sólo me printa un nombre!! Porque??
    #return new_list #Ojo: si idento el return al mismo nivel que if, sólo me printa un en algunos y vacía en otro! Porque??
    return new_list #Solo funciona si idento el return al mismo nivel que el "for" Porque??


# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))


'''Vamos a analizar la función previa línea por línea:

1. def delete_person(person_name):

def: Esta palabra clave indica que estamos definiendo una nueva función.
delete_person: Es el nombre que le damos a la función. En este caso, describe lo que hace: eliminar a una persona.
(person_name): Esto significa que la función necesita un dato para funcionar, que llamamos person_name. Este dato será el nombre de la persona que queremos eliminar de la lista.
2. new_list = []

Creamos una nueva lista vacía llamada new_list. Esta lista almacenará los nombres de las personas que queremos conservar.
3. for name in people:

for: Esta palabra clave inicia un bucle, que nos permite repetir un bloque de código varias veces.
name in people: En cada repetición del bucle, se toma un nombre de la lista people y se le asigna a la variable name.
4. if name != person_name:

if: Esta palabra clave introduce una condición. El código que sigue solo se ejecutará si la condición es verdadera.
name != person_name: Esta es la condición. Se comprueba si el name actual del bucle es diferente al person_name que se pasó a la función.
5. new_list.append(name)

.append(): Esta acción agrega un elemento al final de una lista.
Si el name actual es diferente del person_name, se agrega a la new_list.
6. return new_list

return: Esta palabra clave indica el final de la función y devuelve un resultado.
En este caso, la función devuelve la new_list que contiene todos los nombres excepto el que queríamos eliminar.
En resumen, la función recorre la lista original people, compara cada nombre con el que se quiere eliminar y si son diferentes, los agrega a una nueva lista. Al final, devuelve esta nueva lista'''
