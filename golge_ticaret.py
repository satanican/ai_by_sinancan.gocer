import asyncio
import aiohttp
from datetime import datetime

# Çocuğumuzun Sanal Kasası (Hafıza eklendi)
kasa = {
    "USDT": 100.0,
    "SOL": 0.0,
    "son_alim_fiyati": 0.0  # Kâr/Zarar hesabı için tuttuğumuz hafıza
}

async def dinamik_beyin():
    print("[SİSTEM] Dinamik Zeka (SMA - Hareketli Ortalama) modülü yüklendi.")
    print("[SİSTEM] Matrix'ten son 15 dakikanın grafikleri çekiliyor...")
    print(f"[BAŞLANGIÇ] Kasa: {kasa['USDT']} USDT | {kasa['SOL']} SOL\n")
    
    url_fiyat = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
    url_grafik = "https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m&limit=15"
    
    try:
        async with aiohttp.ClientSession() as session:
            while True:
                # 1. Hafızayı (Son 15 dakikanın kapanış fiyatlarını) çek
                async with session.get(url_grafik) as resp_grafik:
                    grafik_verisi = await resp_grafik.json()
                    kapanislar = [float(mum[4]) for mum in grafik_verisi]
                    sma_15 = sum(kapanislar) / len(kapanislar)
                
                # 2. Gözleri (O anki milisaniyelik fiyatı) çek
                async with session.get(url_fiyat) as resp_fiyat:
                    fiyat_verisi = await resp_fiyat.json()
                    anlik_fiyat = float(fiyat_verisi['price'])
                    
                zaman = datetime.now().strftime("%H:%M:%S")
                
                # STRATEJİ: Ortalamanın %0.1 altına sarkarsa AL, Alışın %0.1 üstüne çıkarsa SAT
                # (Hızlı aksiyon görmen için aralıkları çok dar tuttum)
                hedef_alim = sma_15 * 0.999 
                hedef_satis = kasa["son_alim_fiyati"] * 1.001 if kasa["son_alim_fiyati"] > 0 else sma_15 * 1.001
                
                print(f"[{zaman}] Anlık Fiyat: {anlik_fiyat:.2f} | 15D Ortalama: {sma_15:.2f}")
                
                # --- ALIM KARARI ---
                if kasa["USDT"] > 0:
                    if anlik_fiyat <= hedef_alim:
                        alinan = kasa["USDT"] / anlik_fiyat
                        kasa["SOL"] += alinan
                        kasa["son_alim_fiyati"] = anlik_fiyat
                        kasa["USDT"] = 0.0
                        print(f">>> [KAPİTALİST BİT: AL] Fiyat ortalamanın altına sarktı!")
                        print(f">>> İşlem: {anlik_fiyat:.2f} fiyatından {alinan:.4f} SOL alındı.")
                        print(f"    [KASA] {kasa['USDT']:.2f} USDT | {kasa['SOL']:.4f} SOL\n")
                    else:
                        print(f"    [AV BEKLENİYOR] Alım için pusu hedefine ({hedef_alim:.2f}) düşmesi bekleniyor.")
                
                # --- SATIŞ KARARI ---
                elif kasa["SOL"] > 0:
                    if anlik_fiyat >= hedef_satis:
                        alinan_usdt = kasa["SOL"] * anlik_fiyat
                        kar = alinan_usdt - 100.0
                        kasa["USDT"] += alinan_usdt
                        kasa["SOL"] = 0.0
                        kasa["son_alim_fiyati"] = 0.0
                        print(f">>> [KAPİTALİST BİT: SAT] Kâr hedefine ulaşıldı!")
                        print(f">>> İşlem: {anlik_fiyat:.2f} fiyatından SOL satıldı.")
                        print(f"    [SONUÇ] Toplam Kâr/Zarar: {kar:.2f} USDT")
                        print(f"    [KASA] {kasa['USDT']:.2f} USDT | {kasa['SOL']:.4f} SOL\n")
                    else:
                        print(f"    [KÂR BEKLENİYOR] Satış için kâr hedefine ({hedef_satis:.2f}) çıkması bekleniyor.")
                        
                # 5 saniye bekle, döngüyü tekrarla
                await asyncio.sleep(5)
                
    except Exception as e:
        print(f">>> [SİSTEM HATASI] Frekans koptu: {e}")

if __name__ == "__main__":
    asyncio.run(dinamik_beyin())
