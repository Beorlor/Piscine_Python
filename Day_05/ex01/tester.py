from in_out import outer, square, pow

my_counter = outer(3, square)
print(my_counter())  # 9 (3^2)
print(my_counter())  # 81 (9^2)
print(my_counter())  # 6561 (81^2)
print("---")
another_counter = outer(1.5, pow)
print(another_counter())  # 1.8371173070873836 (1.5^1.5)
print(another_counter())  # 3.056683336818703 ((1.5^1.5)^(1.5^1.5))
print(another_counter())  # 30.42684786675409
