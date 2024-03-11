

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return a list of all pets belonging to the owner
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        # Check if the input is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Please provide an instance of the Pet class.")
        
        # Add the owner to the pet
        pet.owner = self

    def get_sorted_pets(self):
        # Get a sorted list of pets by their names
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        #check if pet_type is valid
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Please provide a valid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)


# Example usage:
owner1 = Owner("John")
owner2 = Owner("Jane")

pet1 = Pet("Buddy", "dog", owner1)
pet2 = Pet("Fluffy", "cat", owner1)
pet3 = Pet("Charlie", "bird", owner2)

# Add a new pet to an owner
owner1.add_pet(Pet("Max", "dog"))

# Get and print the sorted list of pets for owner1
sorted_pets_owner1 = owner1.get_sorted_pets()
print("Owner 1's sorted pets:", [pet.name for pet in sorted_pets_owner1])

