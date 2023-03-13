class Marvel:
    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        
marvel1= Marvel("iron man", 100,10,90)
marvel2= Marvel("thor",110,20,120)
marvel3= Marvel("hulk",115,15,110)

print(marvel1.name)
print(marvel2.health)
print(marvel3.__dict__)