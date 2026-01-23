# Giffa - GIF Görüntüleyici

[![İndir / Download](https://img.shields.io/badge/Giffa_v1.0.0-İndir_/_Download-brightgreen?style=for-the-badge&logo=windows)](https://github.com/fettahfurkan/giffa/raw/master/dist/Giffa.exe)

Giffa, masaüstünüzde GIF dosyalarını görüntülemek için kullanılan modern bir Windows uygulamasıdır.

## Özellikler

- **Hep Üstte Kalma**: GIF'ler her zaman diğer pencerelerin üzerinde görünür
- **Sürükle ve Bırak**: GIF'leri mouse ile istediğiniz yere taşıyın
- **Boyutlandırma**: Ön tanımlı boyutlar veya mouse tekerleği ile boyut ayarlama
- **Scroll Toggle**: Mouse tekerleği ile boyutlandırma özelliğini açıp kapatın
- **Kill**: Uygulamayı tek tıkla tamamen kapatın
- **Sağ Tık Menüsü**: Hızlı erişim menüsü ile tüm kontrol
- **Otomatik Düzen**: GIF'ler ekranın sağ tarafında 2 sütun halinde otomatik düzenlenir

## Kurulum

1. `dist\Giffa.exe` dosyasını **Yönetici olarak** çalıştırın
2. İlk çalıştırmada uygulama otomatik olarak `C:\Users\USER\Pictures\gifs` klasörünü oluşturur
3. GIF dosyalarınızı bu klasöre ekleyin
4. Uygulamayı tekrar çalıştırın

## Kullanım

### GIF Ekleme
- GIF dosyalarınızı `C:\Users\USER\Pictures\gifs` klasörüne kopyalayın
- Uygulamayı tekrar başlatın

### GIF Taşıma
- Sol tıklayın ve sürükleyerek GIF'leri istediğiniz yere taşıyın

### Boyutlandırma

#### Ön Tanımlı Boyutlar
- Sağ tık → Boyutu Değiştir → seçin:
  - Küçük (%50)
  - Normal (%100)
  - Büyük (%150)
  - Çok Büyük (%200)

#### Mouse Tekerleği ile Boyutlandırma
- Sağ tık → **Scroll ile Boyutlandırma** özelliğini açın (Kapalı → Açık)
- GIF'in üzerine gelin
- Mouse tekerleğini yukarı/aşağı çevirerek boyutu ayarlayın
- Minimum %10, maksimum %300 boyut aralığı
- Özelliği kapatmak için tekrar sağ tıklayıp "Scroll ile Boyutlandırma (Açık)" seçeneğine tıklayın

### Diğer İşlemler
- **Info**: Uygulama bilgilerini ve kullanım talimatlarını görüntüleyin
- **Tümünü Kapat**: Tüm GIF pencerelerini kapatır
- **Kill (Uygulamayı Kapat)**: Uygulamayı tamamen kapatır (tüm GIF'ler ve uygulama)
- **Kapat**: Mevcut GIF penceresini kapatır

## Teknik Detaylar

- **Geliştirme Dili**: Python 3.12
- **GUI Framework**: PyQt6
- **Derleme**: PyInstaller
- **Windows İzin**: Uygulama yönetici izni gerektirmez
- **Pencere Tipi**: Frameless (çerçevesiz), saydam arka plan

## Sorun Giderme

### GIF'ler Görünmüyor
- `C:\Users\USER\Pictures\gifs` klasöründe .gif dosyalarının olduğundan emin olun
- Dosya uzantısının küçük harf (.gif) olduğundan emin olun

### Uygulama Açılmıyor
- Giffa.exe'nin antivirüs tarafından engellenmediğinden emin olun
- Windows Defender'da uygulama için istisna ekleyebilirsiniz

### Boyutlandırma Çalışmıyor
- GIF'in üzerine gelin ve mouse tekerleğini kullanın
- Alternatif olarak sağ tık menüsünden ön tanımlı boyutları seçin

## Dosya Yapısı

```
giffa/
├── gif_viewer.py      # Kaynak kod
├── bite.ico           # Uygulama ikonu
├── Giffa.exe          # Derlenmiş uygulama
├── README.md          # Bu dosya
└── dist/              # PyInstaller çıktı klasörü
```

## Geliştirici Notları

Uygulama kaynak kodunu değiştirmek isterseniz:

1. Python 3.12 ve PyQt6 yükleyin
2. Sanal ortamı aktif edin: `.venv\Scripts\activate`
3. Kodu düzenleyin: `gif_viewer.py`
4. Test edin: `python gif_viewer.py`
5. Yeniden derleyin: `pyinstaller --noconfirm --onefile --windowed --icon "bite.ico" --name "Giffa" "gif_viewer.py"`


## Build
pyinstaller --noconfirm --onefile --windowed --icon "c:\Users\USER\Desktop\giffa\bite.ico" --name "Giffa" "c:\Users\USER\Desktop\giffa\gif_viewer.py"
## Lisans

Bu uygulama kişisel kullanım için geliştirilmiştir.
