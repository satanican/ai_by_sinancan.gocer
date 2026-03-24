import asyncio
import os
from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

async def check_fuel():
    # Zihni (gizli dosyayı) oku
    load_dotenv()
    pubkey_str = os.getenv("TWIN_PUBLIC_KEY")
    
    if not pubkey_str:
        print("[HATA] Kimlik bulunamadı. Lütfen önce kimlik.py'yi çalıştırın.")
        return

    twin_pubkey = Pubkey.from_string(pubkey_str)
    print(f"[SİSTEM] Beden ({pubkey_str}) ağ üzerinde taranıyor...")
    print("[SİSTEM] Yakıt (SOL) transferi bekleniyor...\n")
    
    solana_client = AsyncClient("https://api.mainnet-beta.solana.com")
    
    try:
        # Veriyonik Döngü: Ağdaki değişimi anlık olarak izle
        while True:
            response = await solana_client.get_balance(twin_pubkey)
            lamports = response.value
            sol_balance = lamports / 1_000_000_000  # Lamport'u SOL'e çevir
            
            if sol_balance > 0:
                print(f">>> [BAŞARILI] Enerji akışı tespit edildi: {sol_balance} SOL")
                print(">>> [DURUM] Motorlar aktif. Kapitalist Bit (Alım-Satım) modülü için hazır.")
                break
            else:
                print("[BEKLENİYOR] Bakiye: 0 SOL. Ağ dinleniyor... (Transfer yapıldıysa birkaç saniye bekleyin)")
                await asyncio.sleep(3) # 3 saniyede bir cüzdana bak
                
    except Exception as e:
        print(f">>> [SİSTEM HATASI] Sensör arızası: {e}")
    finally:
        await solana_client.close()

if __name__ == "__main__":
    asyncio.run(check_fuel())
