#Solución aquí https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/ 
#Encontrar el número más grande en una lista sin usar funciones integradas

my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(my_list):
    max = my_list[0] # Assume first number in list is largest initially and assign it to variable "max"
    #Initialization step: It sets an initial value for the max_value variable so that we have something to compare against as we iterate through the list.
    #we need a starting point for our comparison. We could technically start with any value (like 0 or a very small number), but using the first element of the list is a convenient choice.
    #In essence, we're not assuming the first value is the maximum, but rather using it as a placeholder to start the comparison process.
#Now traverse through the list and compare each number with "max" value. Whichever is largest assign that value to "max'.
    for number in my_list: #Compare with other elements: We go through the rest of the list, comparing each number with our current max_value.
        if number > max: #Update if a larger number is found: If we find a number bigger than max_value, we update max_value to that new number.
            max = number
    # after complete traversing the list
    # return the "max" value
    return max #Return the final maximum: After checking all numbers, max_value will hold the true maximum value of the list.

print(max_integer(my_list))