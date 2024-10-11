all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def r_name(items):
    return items[0] == "R" 

resulting_names = list(filter(r_name, all_names))
print(resulting_names)




