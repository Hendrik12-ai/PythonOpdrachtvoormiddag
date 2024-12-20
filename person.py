class person:
    def __init__(self, name, age,gender, height, mass, occupation,favorite_food):
        self.name = name
        self.age = age
        self.gender = gender
        self.height =height
        self.mass =mass
        self.occupation = occupation
        self.favorite_food = favorite_food

    def walk(self):
        return f"{self.name} is walking through life. "

    def eat(self, food):
        self.food = food
        return f"{self.name} is eating a {self.food} and loving it. "
    def sleep(self):
        return f"{self.name} is snoozing. And no one dared to Disturb the sound of silence. "
    def work(self):
        return f"{self.name} is going to work as a {self.occupation}. "
    def introduce(self):
         bmi =  self.mass / (self.height* self.height)
         return f"Hello, my name is {self.name}. My BMI is {bmi:.2f}."


def character_menu ():
    print("Welcome to the Character menu!")
    name = input("Enter your character's name: ")
    age = int(input("Enter your character's age: "))
    gender = input("Enter your character's gender: ")
    height = float(input("Enter your character's height (in m): "))
    mass = float(input("Enter your character's mass (in kg): "))
    occupation = input("Enter your character's occupation: ")
    favorite_food = input("Enter your character's favorite food: ")
    character = person(name, age, gender, height, mass, occupation, favorite_food)
    print("\nCharacter creation complete!")
    return character

def doing (character):
    print(character.walk())
    print(character.eat("pizza"))
    print(character.eat("pasta"))
    print(character.sleep())
    print(character.work())
    print(character.introduce())