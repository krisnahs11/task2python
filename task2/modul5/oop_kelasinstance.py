class Marvel:
    # class variable 
    jumlah= 0

    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        # instance variables
        self.name = inputname
        self.health= inputhealth
        self.power= inputpower
        self.armor= inputarmor
        Marvel.jumlah += 1
        print("hero Marvel dengan nama :" + inputname)

marvel1= Marvel("iron man",900,800,700)
print(Marvel.jumlah)
marvel2= Marvel("thor",1200,1000,1000)
print(Marvel.jumlah)
marvel3= Marvel("hulk",1100,1000,1050)
print(Marvel.jumlah)