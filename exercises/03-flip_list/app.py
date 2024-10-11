sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below: ES CORRECTO Y PASA EL TEST!!!

#how to reverse a list using the For Loop + .index()!!!
# https://www.upgrad.com/tutorials/software-engineering/python-tutorial/reverse-list-in-python/
 
new_list = []

for a in sample_list:
    new_list.insert(0,a)

print("initial list: ", sample_list)
print("final list: ", new_list)


#Porque el método de invertir lista que funcionó en ej. previos no funciona aquí y da como resultado initial list = final list??

for a in sample_list[::-1]:
    new_list.insert(0,a)
print("initial list: ", sample_list)
print("final list: ", new_list)