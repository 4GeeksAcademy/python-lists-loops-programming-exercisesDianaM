names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

# Your code here


names[1] = "Steven"
names[-1] = "Pepe"
names[0] = names[2]+names[4]
#Create an empty list to store the reversed elements:
reversed_names = []


#Opción A) Esta debería pasar el test porque además de que el output es que correcto, usa for loop para invertir la lista usando el método que aquí explica Method 5: Reversing a List using the insert() Function
#https://www.upgrad.com/tutorials/software-engineering/python-tutorial/reverse-list-in-python/ 

#Iterate through the original list in reverse order:
for a in names[::-1]:
#Add each element in the original list to the beginning of the new list using the insert() function:
   reversed_names.insert(0,a)
   print(a)


#Opción B) Reverse usando insert() esta opción tampoco pasa el test porque aunque Sí utiliza el For loop para invertir la lista el output NO es correcto:
#To reverse a list using the insert() function in Python, follow these steps: https://www.upgrad.com/tutorials/software-engineering/python-tutorial/reverse-list-in-python/

for a in names:
  reversed_names.insert(0,a)
print(reversed_names)



