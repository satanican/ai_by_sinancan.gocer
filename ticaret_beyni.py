import asyncio
import aiohttp

async def check_market_opportunity():
    print("[SİSTEM] Ticaret Beyni (Küresel Ağ - Binance Oracle) aktif ediliyor...")
    print("[SİSTEM] 'Kapitalist Bit' (Kâr/Zarar) analizi başlatıldı.\n")
    
    amount_in_sol = 0.1
    print(f">>> [HEDEF] {amount_in_sol} SOL piyasaya sürülürse anlık karşılığı ne olur?\n")
    
    # Ambargosuz, devasa küresel ağ bağlantısı
    url = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # Saf fiyat verisini çek
                    sol_price = float(data['price'])
                    out_amount = amount_in_sol * sol_price
                    
                    print(f">>> [KÜRESEL VERİ] 1 SOL = {sol_price:.2f} USDT (Dolar)")
                    print(f">>> [HESAPLANAN] 0.1 SOL = {out_amount:.2f} USDT (Dolar)")
                    
                    print("\n[ANALİZ] Ambargo delindi. Saf veri başarıyla çekildi.")
                    print("[DURUM] Ticaret beyni zihinsel olarak kusursuz çalışıyor.")
                else:
                    print(f">>> [HATA] Ağ reddetti. Kod: {response.status}")
    except Exception as e:
        print(f">>> [SİSTEM HATASI] Frekans koptu: {e}")

if __name__ == "__main__":
    asyncio.run(check_market_opportunity())
