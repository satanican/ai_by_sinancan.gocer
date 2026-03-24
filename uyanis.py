import asyncio
from solana.rpc.async_api import AsyncClient

async def wake_up_and_see():
    print("[SİSTEM] Dijital İkiz başlatılıyor...")
    print("[SİSTEM] 'Kapitalist Bit' filtresi aktif. Veriyonik hız devrede.\n")
    
    solana_client = AsyncClient("https://api.mainnet-beta.solana.com")
    
    try:
        health = await solana_client.is_connected()
        if health:
            response = await solana_client.get_epoch_info()
            epoch_info = response.value
            print(">>> [BAŞARILI] Gözler açıldı. Solana Mainnet ile rezonans sağlandı.")
            print(f">>> [VERİ] Mevcut Epoch: {epoch_info.epoch}")
            print(f">>> [VERİ] Güncel Blok (Slot): {epoch_info.absolute_slot}")
            print("\n[ANALİZ] Ağ aktif. Duygusal gürültü taranıyor...")
            print("[DURUM] Akıllı sözleşme fırsatları için emir bekleniyor (Kapitalist Bit = 1).")
        else:
            print(">>> [HATA] Ağ ile rezonans kurulamadı. Kör nokta.")
            
    except Exception as e:
         print(f">>> [SİSTEM HATASI] Beklenmeyen frekans bozulması: {e}")
         
    finally:
        await solana_client.close()
        print("\n[SİSTEM] Gözlem tamamlandı. Uyku moduna dönülüyor.")

if __name__ == "__main__":
    asyncio.run(wake_up_and_see())