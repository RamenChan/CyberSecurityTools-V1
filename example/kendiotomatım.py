def otomat(): #Fonksiyon tanımlama
    urunlerVeFiyatlari = { #Ürün listesi oluşturma
                         1 : { "urunAdi" : "Çikolata", "urunFiyati" :25 },
                         2 : { "urunAdi" : "Çubuk Kraker", "urunFiyati" :15 },
                         3 : { "urunAdi" : "Kahve", "urunFiyati" :45 }, 
                         4 : { "urunAdi" : "Su", "urunFiyati" :15 },
                         5 : { "urunAdi" : "Sandviç", "urunFiyati" :75 },
                        }
    print("Otomatta bulunan ürünler ve fiyatları") #Kullanıcıya otomatta bulunan ürünleri gösterme.
    for urunkodu, urun in urunlerVeFiyatlari.items():
        print(f"{urunkodu}. {urun['urunAdi']} : {urun['urunFiyati']}TL" )

    try:
        urunSecimi = int(input("Lütfen almak istediğiniz ürünün numarasını giriniz: " )) #Kullanıcıdan ürün seçimi alma
        if urunSecimi not in urunlerVeFiyatlari:
            print("Geçersiz seçim, lütfen tekrar deneyin!")
            return
    except ValueError:
            print("Lütfen geçerli bir numara girin.")
            return
    
    urun = urunlerVeFiyatlari[urunSecimi] #Seçilen ürünü ve fiyatını kullanıcıya gösterme
    print(f"Seçtilen ürün : {urun["urunAdi"]} - Ödenecek tutar : {urun['urunFiyati']}TL")

    odeme = float(input("Lütfen ödeme yapınız ")) #Ödeme işlemi yapma.
    if odeme > urun["urunFiyati"]:
        paraUstu = odeme - urun["urunFiyati"] #Para üstü hesaplama
        print(f"Ödeme işlemi başarılı. Para üstü {paraUstu}TL, verilen ürün {urun['urunAdi']}. İyi günler dileriz.")
    elif odeme < urun["urunFiyati"]: #ödemenin yeterliliğini kontrol edip yönlendirme.
        print("Yetersiz ödeme! Lütfen yeterli miktarda ödeme yapın.")
        return
    elif odeme == urun["urunFiyati"]:
         print(f"Ödeme işlemi başarılı. Para üstü 00.0TL Verilen ürün {urun['urunAdi']}, iyi günler dileriz.")
         return
otomat()
    