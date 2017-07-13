list_a = ["a", "dd", "J", "L", "Apple"]
print("unsorted: ", list_a)
list_a.sort(key=str.lower, reverse=True)
print(list_a)

list_b = ["Apple", "plum", "kiwi", "BANANA"]
print("unsorted: ", list_b)
print(sorted(list_b))
