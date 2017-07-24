a_list = ["Test1", 1, "Apple", 65, "Another String", "44", 23, "A String"]
number_list = []
x = 0

for item in a_list:
    if isinstance(item, int):
        #number_list.append(item)
        #a_list.pop(x)
        number_list.append(a_list.pop(x))
    else:
        print(item, " is not an integer ")

    x += 1

print(number_list)
print(a_list)
