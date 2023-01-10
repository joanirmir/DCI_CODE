

class Animal:
    # constructor 
    # defines the rules on how to create an instance of a class
    def __init__(self, eyes, ears, legs, tail, fur):
        # set the class instance variables
        # classes
        # private instance variable?
        self.eyes = eyes
        self.ears = ears
        self.legs = legs
        self.tail = tail
        self.fur = fur

    # TODO: other methods later
    def __repr__(self):
        return f"Eyes: {self.eyes}, Ears: {self.ears}, Legs: {self.legs}, Tail: {self.tail}, Fur: {self.fur}"

# how to inherit from another class
class Person(Animal):
    def __init__(self, eyes, ears, legs, tail, fur, city):
        # hint: super()
        super().__init__(eyes, ears, legs, tail, fur)
        self.city = city


if __name__== '__main__':
    person_a = Person(2,2,2,0, 'nothing', 'Berlin')
    animal_a = Animal(2,2,4,1, 'yes')
    print(person_a)
    print(animal_a)