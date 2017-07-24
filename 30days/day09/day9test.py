from messageUser import MessageUser

obj = MessageUser()
obj.add_user("Justin", 123.32, "hello@gmail.com")
obj.add_user("john", 94.23)
obj.add_user("Emilee", 124.32)
obj.add_user("Jim", 323.4)
obj.add_user("Ron", 23)
obj.add_user("Sandra", 322.122323)
obj.add_user("veronica", 32.4)
obj.add_user("Whitney", 99.99)

#print(obj.get_details())
print(obj.make_messages())


#default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
#default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]
