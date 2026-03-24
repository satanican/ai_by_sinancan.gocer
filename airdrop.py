import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

async def get_synthetic_fuel():
    print("[SİSTEM] Simülasyon Evrenine (Solana Devnet) geçiş yapılıyor...")
    
    # İkizimizin yeni yarattığımız bedeni
    pubkey_str = "9tbQaU99Vbg6f9xsPKyYdzXi2HArZ7KR72cXM2fsBJ3C"
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
