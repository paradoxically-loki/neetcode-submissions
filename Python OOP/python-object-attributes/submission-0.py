class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

# TODO: Print Whiskers' modified attributes
print(f"Initial Attributes: Whiskers ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

whiskers.hunger = 3
whiskers.energy =  10

print(f"Modified Attributes: Whiskers ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

