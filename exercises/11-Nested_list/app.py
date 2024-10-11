coordinates_list = [[33.747252, -112.633853], [-33.867886, -63.987], [41.303921, -81.901693], [-33.350534, -71.653268]]
#OJO: si defino la variable longitud fuera, me imprime solo la longitud con índices [0][1] (primera sublista, segundo argumento)
# longitudes = coordinates_list[0][1]

# Your code here
for coordinate in coordinates_list:
    longitudes = coordinate[1]#con esto le digo que de la lista anidada coordinates_list, la longitud es el 2o argumento (índice [1]9 de cada sublista (o "coordinate")
    #longitudes = coordinates_list[0] #me imprim longitud y latitud de la primera coordenada tantas veces como coordenadas hay en la lista paraguas
    print(longitudes)

