ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
         
ft_list[1] = "World!"

ft_tuple = (ft_tuple[0], "France!")

ft_set.remove("tutu!")   # remove the old string
ft_set.add("Paris!")     # add the new string

# For dict, change the value associated with the key "Hello"
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
