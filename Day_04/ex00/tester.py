from S1E9 import Character, Stark

# Create a Stark instance
Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")

# Create another Stark instance with different initial state
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

# Ensure Character cannot be instantiated
try:
    hodor = Character("hodor")
except TypeError:
    print("TypeError: Can't instantiate abstract class Character with "
          "abstract method")
