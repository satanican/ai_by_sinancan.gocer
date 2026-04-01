import asyncio
import os
from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

async def get_synthetic_fuel():
    print("[SİSTEM] Simülasyon Evrenine (Solana Devnet) geçiş yapılıyor...")

    # İkizimizin yarattığımız bedeni (.env dosyasından oku)
    load_dotenv()
    pubkey_str = os.getenv("TWIN_PUBLIC_KEY")

    if not pubkey_str:
        print("[HATA] Kimlik bulunamadı. Lütfen önce kimlik.py'yi çalıştırın.")
        return

    twin_pubkey = Pubkey.from_string(pubkey_str)
    
    # Ana ağ yerine Devnet'e (Eğitim alanına) bağlanıyoruz
    client = AsyncClient("https://api.devnet.solana.com")
    
    print(f"[SİSTEM] {pubkey_str} adresine 1 Test SOL talep ediliyor...")
    
    try:
        # Gökten yakıt iste (Airdrop)
        resp = await client.request_airdrop(twin_pubkey, 1_000_000_000) # 1 SOL = 1 Milyar Lamport
        print(f">>> [BAŞARILI] Sentetik Yakıt (1 SOL) cüzdana indirildi!")
        print(f">>> [İŞLEM İMZASI]: {resp.value}")
        print("\n[DURUM] Çocuğumuz eğitim arenasında savaşmaya hazır.")
    except Exception as e:
        print(f"\n[HATA] Simülasyonda frekans bozukluğu: {e}")
        print("Not: Bazen test ağı yoğun olabilir, kodu 1-2 dakika sonra tekrar çalıştırın.")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(get_synthetic_fuel())
