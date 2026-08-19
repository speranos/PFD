ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "world!"
ft_tuple = ("Hello", "Morocco!")
ft_set = {"Hello", "Ben Guerir!"}
ft_dict["Hello"] = "1337!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


# Need order + mutability? → List
# Need order + immutability? → Tuple
# Need unique items only? → Set
# Need key-value mapping? → Dictionary