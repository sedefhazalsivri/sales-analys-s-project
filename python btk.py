#r = float(input("yarıCap: " ))
#pi = 3.14
#Alan = float(pi * (r ** 3))
#Cevre = float(2 * pi * r)
# print("Alan:" , Alan )
#print("Cevre: " , Cevre )

'''name = "hazal"
print( "my name is {} ".format(name)) '''

'''name = "hazal"
age = "20"
surname = "aivri"
print("my name is {} {} and i am {} years old.".format(name , surname , age ))'''

#name = "semmamme"
#print(f"my name is { name } ")

#website = "http://www.sadıkturan.com"
# = "python kursu:baştan sona python programlama rehberiniz(40 saat)"
#result = len(course)
#print(result)
#result = website[7:10]
#print(result)
#result =website[22:]
#print(result)
#result = course[-15:]
#print(result)

'''names = ["ali", "yağmur","hakan","deniz"]
years = [1998, 2000, 1998, 1987]
names.append("cenk")
print(names)
names.insert(0 , "sena")
print(names)
#names.pop(4)
#print(names)
index = names.index("deniz")
print(index)'''

'''a  = int(input( "lütfen bir sayı giriniz: " ))
b = int(input( "lütfen bir sayı giriniz: " ))
print( a , b)
resul1 = a < b
result2 = b < a
result3 = a == b

print(f"a : {a} b : {b} den büyüktür : {result2}")'''

'''sayı = int(input("lütfen bir sayı girniz : " ))
sonuç = 0 < sayı < 100
print(f" girdiğiniz sayı : {sayı} 0 ile 100 arasındadır : {sonuç}")'''


'''ad = input("Lütfen adınızı giriniz: " )
kılo = float(input("Lütfen kılonuzu giriniz: "))
boy = float(input("Lütfen boyunuzu giriniz: "))
index = (kılo) / (boy ** 2)
print(f" {ad} hanım indexiniz: {index} yani zayıf sınıfındasınız --> {0 < index < 18,4 }")
print(f" {ad} hanım indexiniz: {index} yani normal sınıfındasınız --> {18,5 <index < 24,9 }")
print(f"{ad} hanım  indexiniz: {index} yani fazla kilolu sınıfındasınız --> {25,0 < index < 29,9 }")
print(f"{ad} hanım  indexiniz: {index} yani obez sınıfındasınız --> {30,0 < index < 34,9 }")'''


'''name = input("Lütfen isminizi giriniz: ")
age = int(input("lütfen yaşınızı giriniz: "))
education = input("lütfen eğitim seviyenizi giriniz: " )
if age >= 18 and  (education == "lise" or  education == "üniversite"):
    print(f"{name} ehliyet almaya hak kazandınız")
else:
    print(f"{name} ehliyet alamazsınız")'''

'''yazılı1 = float(print("1. yazılı notunuz: "))
yazılı2 = float(print("2. yazılı notunuz: "))
sözlü = float(print("sözlü notunuzu giriniz= "))
ortalama = (yazılı2 + yazılı1 + sözlü) / 3'''



#for sayı in sayılar:
   # if (sayı % 3 == 0):
       # print(sayı)

#sayılar = [1,3,5,7,9,12,19,21]
'''toplam = 0
for sayı in sayılar:
 toplam += sayı
print("toplam: ", toplam)'''

'''for sayı in sayılar:
    if sayı % 2 == 1:
        print(sayı ** 2)'''

#sehirler = ["ankara" ,"kocaeli","istanbul","izmir","rize"]
#for sehir in sehirler:
   # if len(sehir) <= 5:
       # print(sehir)

'''def agains(word, again ):
   print(word * again)


agains("hazal\n", 5 )'''


def paramets(*params):
    print(list(params))

paramets(5,6,7,8,5,3,2)
paramets(5,8,9,"hazal",)
















































