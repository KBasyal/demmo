#learning class
class person():
    name = "kamal"
    occupation = "Software developer"
    net_worth = 2000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

b = person()
print(b.name,b.occupation)
b.info()


#creating another class and object to practice more

class nepal():
    citizens="neplese"
    national_animale="cow"
    national_bird="Lhophophorus"
    def citizen(self):
        print(f"The nationality of people living in Nepal is {self.citizens}")

nation= nepal()

print(nation.national_animale)

nation.citizen()

