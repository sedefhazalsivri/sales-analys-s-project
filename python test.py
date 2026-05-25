   isim = input("adınız nedir? ")
  print("merhaba "+ isim)

   yemek = input("en sevdiğiniz yemek nedir? ")
   print(isim+ " " + yemek + " sever")

  x = input("bir sayı giriniz ")

  y = input("bir sayı daha giriniz ")

  print( int(x) + int (y))

  isim = "semmamme"
  print(isim[-1])
  print(isim[-3:-1])

  isim = input( "adınız nedir? ")
  print(isim.title())



  "18 yaşından büyük" == True
  "okula gidiyor" == True


    if "18 yaşından büyük" and not "okula gidiyor":
        print("askere gelme yaşınız geldi!")

    elif "okula gidiyor" and "18 yaşından büyük":
        print("okulunuz bittiğinde askere geleceksiniz")

    else:
        print("askerlik yaşınız daha gelmedi!")


"ilk sayı" == int(input( " lütfen ilk sayıyı giriniz."))
"ikinci sayı" == int(input(" lütfen ikinci sayıyı giriniz."))
"işlem" == input( """ lütfen yapacağınız işlemi seçiniz.
      (toplama = "+", çıkarma = "-", bölme = "/", çarpma = "x")""")

if "işlem" == "+" :
    print("sonuç: " + str("ilk sayı"+"ikinci sayı"))

elif "işlem" == "-" :
    print("sonuç: " + str( "ilk sayı"-"ikinci sayı"))

elif "işlem" == "/" :
    print("sonuç: " + str( "ilk sayı"/"ikinci sayı"))

elif "işlem" == "x" :
    print( "sonuç: " + str( "ilk sayı"*"ikinci sayı"))



    import math
