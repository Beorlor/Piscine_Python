from S1E7 import Baratheon, Lannister

# Test Baratheon
Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")

# Test Lannister
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")

# Create a Lannister using the class method
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : ({Jaine.first_name}, {Jaine.family_name}),"
      f" Alive : {Jaine.is_alive}")
