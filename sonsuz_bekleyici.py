#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Trafik Işığı Bekleyicisi
Yeşil asla yanmaz. Bu bir özelliktir, bug değil.
"""

import time
import random
import sys

def felsefi_nutuk():
    nutuklar = [
        "Beklemek, varlığın en saf halidir.",
        "Yeşil ışık bir illüzyondur, kırmızı gerçektir.",
        "Saniyeler geçiyor ama ben hala buradayım. Bu da bir zafer.",
        "Evrende herkes bir şeyi bekliyor. Ben trafik ışığını seçtim.",
        "Durmak, ilerlemenin en yüksek formudur. (Belki.)"
    ]
    return random.choice(nutuklar)

def main():
    print("=== SONSUZ TRAFİK IŞIĞI BEKLEYİCİSİ BAŞLATILDI ===")
    print("Kırmızı yanıyor. Ve yanmaya devam edecek.")
    print("Durdurmak için Ctrl+C bas, ama aslında basma. Bekle.\n")
    
    saniye = 0
    try:
        while True:
            saniye += 1
            print(f"[{saniye} saniye] Kırmızı ışıkta bekleniyor... {felsefi_nutuk()}")
            
            if random.random() < 0.05:  # %5 ihtimalle yalan söyle
                print(">>> YEŞİL YANDI! HAYIR, YALAN. HALA KIRMIZI. <<<")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBekleme durduruldu. Ama trafik ışığı hala kırmızı. Kaçış yok.")
        sys.exit(0)

if __name__ == "__main__":
    main()
