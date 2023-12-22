import random

def yilbasi_cekilisi(kisiler):
    # Eşleştirmeleri tutacak bir sözlük oluştur
    eslestirmeler = {}

    # Kişileri karıştır
    random.shuffle(kisiler)

    # Her kişi için eşleşme oluştur
    for i in range(len(kisiler)):
        eslestirmeler[kisiler[i]] = kisiler[(i + 1) % len(kisiler)]

    return eslestirmeler

# Katılımcı isimlerini liste olarak belirt
katilimcilar = ["Ali", "Altay", "Onur"]

# Çekilişi yap ve sonuçları al
sonuclar = yilbasi_cekilisi(katilimcilar)

# Sonuçları ekrana yazdır
for katilimci, hediye_alacak_kisi in sonuclar.items():
    print(f"{katilimci} --> {hediye_alacak_kisi}")
