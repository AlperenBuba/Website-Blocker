import ctypes
import time
import os

# --- AYARLAR ---
# Bu kelime URL içinde veya başlıkta bitişik olsa bile (örn: xfilmizyonx.com) tetiklenir.
YASAKLI_KELIME = "filmizyon"

# Kapatılacak tarayıcı listesi
TARAYICILAR = ["msedge.exe", "chrome.exe", "opera.exe", "brave.exe", "firefox.exe"]

def get_all_window_texts():
    """Bilgisayardaki tüm pencerelerin ve içindeki metin alanlarının başlıklarını toplar."""
    titles = []
    def callback(hwnd, extra):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
            if buff.value:
                titles.append(buff.value.lower())
        return True

    ENUM_WINDOWS_PROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
    ctypes.windll.user32.EnumWindows(ENUM_WINDOWS_PROC(callback), 0)
    return titles

def imha_et():
    """Tüm tarayıcıları sessizce kapatır."""
    for tarayici in TARAYICILAR:
        os.system(f"taskkill /f /im {tarayici} >nul 2>&1")

def muhafiz_dongusu():
    while True:
        try:
            # Tüm sistemdeki pencere metinlerini ve başlıkları tara
            metinler = get_all_window_texts()
            
            for metin in metinler:
                # 'filmizyon' kelimesi metnin neresinde olursa olsun yakalar
                if YASAKLI_KELIME in metin:
                    imha_et()
                    # Bilgisayarı kasmaması ve arka arkaya binlerce kez çalışmaması için
                    time.sleep(2) 
                    break
        except:
            pass
        
        # Saniyede 5 kez kontrol (0.2 saniye) - Kaçırması imkansızdır.
        time.sleep(0.2)

if __name__ == "__main__":
    # Konsol penceresi olmadan başlar
    muhafiz_dongusu()
