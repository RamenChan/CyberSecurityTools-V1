# islemler.py

def dort_islem():
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        print(f"Toplama: {sayi1 + sayi2}")
        print(f"Çıkarma: {sayi1 - sayi2}")
        print(f"Çarpma: {sayi1 * sayi2}")
        
        if sayi2 != 0:
            print(f"Bölme: {sayi1 / sayi2}")
        else:
            print("Bölme işlemi için ikinci sayı sıfırdan farklı olmalıdır.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

# İşlemi çalıştır
if __name__ == "__main__":
    dort_islem()
