class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        self.pet_type=pet_type
        self._owner=None
        self.owner=owner
        if owner is not None:
            owner.add_pet(self)
        Pet.all.append(self)
    @property
    def pet_type(self):
        return self._pet_type#underscore indicates that _pet_type is intended for internal use within the class
                            #avoids an infinite loop
                            #Using self._pet_type allows us to distinguish between the public property and the internal variable that actually stores the value.
    @pet_type.setter
    def pet_type(self,pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"The pet_type is restricted to this list: \n {', '.join(Pet.PET_TYPES)} ")
        self._pet_type=pet_type
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if owner is not None:
            if not isinstance(owner, Owner):
                raise TypeError("Owner must be an instance of class Owner")
            owner.add_pet(self)
        self._owner = owner

class Owner:
    def __init__(self,name):
        self.name=name
        self._pets=[]
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError("Pet must be an instance of class Pet")
        pet._owner=self
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets,key=lambda p:p.name)
    def pets(self):
        return self._pets
    