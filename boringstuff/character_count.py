import pprint

message = 'dfjkjgh sdfhkjshg hgsjkfdhg kjfdkgk asdheowryo djfhsaidf '
count = {}

for character in message.lower():
	count.setdefault(character, 0)
	count[character] += 1

pprint.pprint(count)