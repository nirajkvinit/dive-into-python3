items = ["Mic", 42, "Apple", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 1234]
print(items)


def parse_lists(some_list):
	str_items = []
	num_items = []
	for i in some_list:
		if isinstance(i, float) or isinstance(i, int):
			num_items.append(i)
		elif isinstance(i, str):
			str_items.append(i)
		else:
			pass
	return str_items, num_items

print(parse_lists(items))

def my_sum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int):
			total += i
	return total

print(my_sum(items))

def count_nums(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += 1
    return total

def my_avg(my_num_list):
	the_sum = my_sum(my_num_list)
	num_of_items = len(my_num_list)
	return the_sum / (count_nums(my_num_list) * 1.0)

print(my_avg(items))
