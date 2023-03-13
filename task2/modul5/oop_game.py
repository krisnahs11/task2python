class Marvel:
   

    def __init__(self, name, health, attackpower, armornumber):
        # instance variables
        self.name = name
        self.health= health
        self.attackpower= attackpower
        self.armornumber= armornumber
    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackpower)

    def diserang(self, lawan, attackpower_lawan):
        print(self.name + " diserang " + lawan.name)
        attact_diterima = attackpower_lawan
        print("serangan terasa : " + str(attact_diterima))
        self.health -= attact_diterima
        print(" darah " + self.name + " tersisa " + str(self.health))

ironman= Marvel("iron man", 100, 10, 5)
hulk = Marvel(" hulk ",110,25,25)

ironman.serang(hulk)