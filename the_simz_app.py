from person44 import  person, character_menu, doing
my_person = person("Vin Diesel", 57,"male", 1.82, 102, "actor", "Italian")
def doing2 ():
    print(my_person.walk())
    print(my_person.eat("pizza"))
    print(my_person.eat("pasta"))
    print(my_person.sleep())
    print(my_person.work())
    print(my_person.introduce())
doing2()
character = character_menu()
doing(character)