my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

new_list = []


#no funciona:

for a in my_list:
    if type(a) == 'dict':
        sum += int(a)
        print(new_list[a])
    elif type(a) == 'list':
        sum += int(age)
        print(new_list[a])
   
print(my_list)    



#no funciona:

for a in my_list:
    if type(a) == 'dict':
        print(new_list.append(a))
    elif type(a) == 'list':
        print(new_list.append(a))
        print(a)

print(new_list)    

# Your code here

#tampoco funciona:

def new_list():
    for a in my_list:
        if type(a) == 'dict':
            print(a)
        elif type(a) == 'list':
            print(a)
    return a

new_list()

#tampoco funciona:
def new_list():
 for a in my_list:
  if type(a) == 'dict':
   print(a)
  elif type(a) == 'list':
   print(a)

print(new_list())


for x in my_list:
    print(x)

#More on type() function here https://www.w3schools.com/python/ref_func_type.asp
#type(object, bases, dict)
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33
d = {"hola": "saludo"}

x = type(a)
y = type(b)
z = type(c)
y = type(d)



