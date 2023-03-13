class Marvel:
    #class variabel
    jumlah_marvel= 0 

    def __init__(self, inputname, inputhealth, inputpower, inputarmor):
        # instance variables
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        Marvel.jumlah_marvel += 1

    # void function, method tanpa return
    def siapa(self):
            print("Namaku adalah :" + self.name)

    # method dengan argumen
    def HealthTambah(self, tambah):
         self.health += tambah

    # method dengan return
    def getHealth(self):
         return self.health

marvel1 = Marvel("iron man",1000,900,800)
marvel2 = Marvel("thor",900,1000,900)


# pemanggilan method
marvel1.siapa()

#pemakaian method dengan argumen
marvel1.HealthTambah(10)
print(marvel1.health)

#mengembaliakn nilai dengan method
print(marvel1.getHealth())