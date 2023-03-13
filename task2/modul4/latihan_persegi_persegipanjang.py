def persegipanjang(panjang,lebar):
    luas= panjang*lebar
    print("luasnya :", luas)
    return luas

def persegi(sisi):
    luas= sisi*sisi
    print("luasnya",luas)
    return luas

print("menghitung luas persegi panjang dan persegi")
print("persegi panjang")
a= int (input("masukan panjang :"))
b= int(input("masukan lebar :"))
persegipanjang(a,b)

print("persegi")
s= int (input("masukan sisi: "))
persegi(s)