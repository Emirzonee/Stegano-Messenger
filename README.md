	# Stegano Messenger

Python tabanlı, görsellerin piksel verileri içerisine gizli metin saklamayı sağlayan ileri seviye bir **Steganografi** aracıdır.

Bu proje, **LSB (Least Significant Bit)** algoritmasını kullanarak, bir resmin görsel kalitesini bozmadan veriyi piksellerin içerisine gömer. Dışarıdan bakıldığında orijinal resim ile şifreli resim arasında hiçbir fark görülmez.

---

##  Özellikler
* **Veri Gizleme (Encode):** PNG/JPG görsellerinin içine metin saklar.
* **Veri Okuma (Decode):** Şifreli görseli analiz ederek saklanan metni çözer.
* **Algoritma:** Bit seviyesinde manipülasyon (Bitwise Operations) kullanır.
* **CLI Tabanlı:** Komut satırı argümanları ile hızlı ve otomatize çalışır.

---

## Kurulum

Projeyi kaynak koddan çalıştırmak isterseniz:

1. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt

# Şifrelemek için (Encode)
python stegano.py encode araba.jpg "!!!"

# Çözmek için (Decode)
python stegano.py decode secret_output.png

Exe olarak kullanma: pyinstaller --onefile stegano.py
Antivirüsler engelleme yapabilir, false positive.. dilerseniz FUD ile şifreleyebilirsiniz.
Resmi zip olarak veya wp den belge olarak, mail ile gönderiniz resmin boyutundaki değişiklik mesajımızı yok eder.
Çalıştırmak için .\stegano.exe decode secret_output.png (powershell içindir, CMD için .\ kaldırınız.)
Bu araç, data hiding öğrenilmesi amacıyla geliştirilmiştir. Başka sebeplerle kullanılmamalıdır.
Emircan BİNGÖL
