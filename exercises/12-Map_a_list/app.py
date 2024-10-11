celsius_values = [-2, 34, 56, -10]

def celsius_to_fahrenheit(celsius_values):
    return celsius_values * 9/5 + 32
    # The magic happens here
   
result = list(map(celsius_to_fahrenheit, celsius_values))

print(result)
