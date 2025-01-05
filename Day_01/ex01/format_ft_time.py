# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jedurand <jedurand@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/05 06:00:02 by jedurand          #+#    #+#              #
#    Updated: 2025/01/05 06:00:02 by jedurand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime

# Temps écoulé depuis le 1er janvier 1970
timestamp = datetime.now().timestamp()

print(
    f"Seconds since January 1, 1970: {timestamp:.4f} "
    f"or {timestamp:.2e} in scientific notation"
)
print(datetime.now().strftime("%b %d %Y"))
