chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']
merged = []

def merge_list(list1, list2):
    # Your code here
    for name in chunk_one:
        merged.append(name)
    for name in chunk_two:
        merged.append(name)
    return merged


print(merge_list(chunk_one, chunk_two))
