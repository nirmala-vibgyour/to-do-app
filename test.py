s = ["hello", "world", "tyra"]
t = "hello"
print(list(enumerate(t)))
print(list(enumerate(s)))

my_list = ["s", "k", "c"]
# here, the change is on the list
# itself can never be stored in itself or in new variable
my_list.append("a")
my_list.append("p")
# my_list.append() returns None type so it is never required
# to store it. With such methods, rather change is made and
# then stored in new variable. something like that.
my_new_list = []
my_new_list += my_list

print(my_new_list)




