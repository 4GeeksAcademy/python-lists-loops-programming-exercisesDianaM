all_numbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]


def filter_function(item): #Fijate que utiliza item en lugar de all_numbers tanto en el nombre de la función como en el return
    #esto es porque tanto map() como filter() ya se aplican por defecto a todos los items de una lista sin añadir For item in list!!!
    # Update here
    return item > 10
    #return item % 2 == 1 THIS FILTERS ODD NUMBERS
    
greater_than_ten = list(filter(filter_function, all_numbers))

print(greater_than_ten)
