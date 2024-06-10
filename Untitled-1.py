print("İşlem seçin: ")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

def toplama(a,b):
    sonuc = a+b
    return sonuc

def cikarma(a,b):
    sonuc = a-b
    return sonuc

def carpma(a,b):
    sonuc = a*b
    return sonuc

def bölme(a,b):
    sonuc = a/b
    return sonuc

while True:
    secim = input("İşlem seçin (toplama/çıkarma/çarpma/bölme): ")


    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))

    if secim == 'toplama':
        print(toplama(a=sayi1,b=sayi2))

    elif secim == 'çıkarma':
        print(cikarma(sayi1,sayi2))
    elif secim == 'çarpma':
        print(carpma(sayi1,sayi2))
    elif secim == 'bölme':
        print(bölme(sayi1,sayi2))
    else:
        print("Geçersiz işlem")
