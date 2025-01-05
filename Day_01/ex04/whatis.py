# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jedurand <jedurand@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/05 06:00:49 by jedurand          #+#    #+#              #
#    Updated: 2025/01/05 06:00:49 by jedurand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # everything after the script name

    if len(args) == 0:
        sys.exit(0)

    if len(args) > 1:
        raise AssertionError("more than one argument is provided")

    single_arg = args[0]

    try:
        number = int(single_arg)
    except ValueError:
        raise AssertionError("argument is not an integer")

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
