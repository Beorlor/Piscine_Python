# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jedurand <jedurand@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/05 06:00:44 by jedurand          #+#    #+#              #
#    Updated: 2025/01/05 06:00:44 by jedurand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(obj: any) -> int:
    """
    Prints the type of 'obj' with a specific format,
    then returns 42.
    """
    # Check for each type or condition
    if isinstance(obj, list):
        print(f"List : {type(obj)}")
    elif isinstance(obj, tuple):
        print(f"Tuple : {type(obj)}")
    elif isinstance(obj, set):
        print(f"Set : {type(obj)}")
    elif isinstance(obj, dict):
        print(f"Dict : {type(obj)}")
    elif isinstance(obj, str):
        # Check if the string is "Brian" or "Toto"
        if obj == "Brian":
            print(f"Brian is in the kitchen : {type(obj)}")
        elif obj == "Toto":
            print(f"Toto is in the kitchen : {type(obj)}")
        else:
            print("Type not found")
    else:
        print("Type not found")

    return 42


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
