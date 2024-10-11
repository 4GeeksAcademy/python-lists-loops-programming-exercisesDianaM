my_sample_list = [3423,5,4,47889,654,8,867543,23,48,5345,234,6,78,54,23,67,3,6,432,55,23,25,12]


def sum_all_values(list):
    for a in my_sample_list:
      total = sum(my_sample_list)

    # The magic happens here
    
    return total
    
print(sum_all_values(my_sample_list))


#Duda: como sería manteniendo el total = 0 como en el código original???


#Codigo original:

my_sample_list = [3423,5,4,47889,654,8,867543,23,48,5345,234,6,78,54,23,67,3,6,432,55,23,25,12]


def sum_all_values(list):
   total = 0


   # The magic happens here

  
   return total
  
print(sum_all_values(my_sample_list))


#Este también funciona pero no contiene for loop y no pasa el test:

def sum_all_values(list):
    total = sum(my_sample_list)

    # The magic happens here


    return total
    
print(sum_all_values(my_sample_list))

