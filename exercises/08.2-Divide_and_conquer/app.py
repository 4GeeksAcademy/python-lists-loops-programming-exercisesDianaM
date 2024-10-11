list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
sorted_list = []
even = []

def sort_odd_even(list_of_numbers):
    for number in list_of_numbers:
        if number % 2 != 0:
            sorted_list.append(number)
        if number % 2 == 0:
            even.append(number)
    sorted_list.extend(even) #Ojo porque si la identación del return no está al mismo nivel que el for no funciona!!!
    return sorted_list

print(sort_odd_even(list_of_numbers))

#Ver todos los intentos fallidos previos y explicaciones varias aquí https://colab.research.google.com/drive/1Xp38FGaN6gaMw3bfGMZnM9l9uSwlns-0?authuser=1#scrollTo=UvqxG7gQTb-9