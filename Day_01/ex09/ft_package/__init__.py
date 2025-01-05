# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jedurand <jedurand@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/05 06:01:11 by jedurand          #+#    #+#              #
#    Updated: 2025/01/05 06:01:11 by jedurand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
ft_package
This is a sample test package for the Piscine Python.
"""

# métadonnées
__version__ = "0.0.1"
__author__ = "jedurand"
__license__ = "MIT"

# On importe la fonction du module core pour la rendre disponible au top-level
from .core import count_in_list
