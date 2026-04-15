class Father():
    def skills(self):
        print("Gardening is my job, my name is Bob")
class Mother():
    def skills(self):
        print("I make you new dishes")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I can count till 10")


child = Child()
child.skills()