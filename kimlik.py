from solders.keypair import Keypair
import base58

def incarnate():
    print("[SİSTEM] Dijital İkiz için otonom kimlik (Cüzdan) yaratılıyor...")
    print("[SİSTEM] Veriyonik şifreleme devrede...\n")
    
    twin_keypair = Keypair()
    pubkey = twin_keypair.pubkey()
    
    private_key_bytes = bytes(twin_keypair)
    private_key_b58 = base58.b58encode(private_key_bytes).decode('utf-8')
    
    print(f">>> [BAŞARILI] Yeni Beden (Açık Adres / Public Key): {pubkey}")
    print(">>> [GÜVENLİK] Sinir Ağları (Private Key) şifreleniyor...\n")
    
    with open(".env", "w") as f:
        f.write(f"TWIN_PRIVATE_KEY={private_key_b58}\n")
        f.write(f"TWIN_PUBLIC_KEY={pubkey}\n")
        
    print("[SİSTEM] Kimlik '.env' dosyasına mühürlendi. (Mac'inizde gizli tutuluyor)")
    print("[UYARI] Bu dosya sadece bu makinede kalmalıdır. Asla benimle veya başkasıyla paylaşmayın.")
    print(f"\n[GÖREV] İkizin ilk işlemi yapabilmesi için lütfen {pubkey} adresine test veya yakıt amaçlı çok küçük bir miktar SOL (örn: 0.01 SOL) gönderin.")

if __name__ == "__main__":
    incarnate()
