class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f'The {self.name} says "{self.sound}"'


lion = Animal(name="lion", sound="roar")
# print(lion)
