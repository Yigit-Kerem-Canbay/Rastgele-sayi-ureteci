# QDSNG - Quadratic Discrete Stochastic Number Generator

## Proje Açıklaması

QDSNG, Python programlama dili ile geliştirilmiş bir kuadratik rastgele sayı üreteci sistemidir. Bu sistem, belirli bir algoritma kullanarak rastgele tamsayılar üretir ve çeşitli uygulamalarda kullanılabilir.

## Özellikler

- **Rastgele Sayı Üretimi**: Belirtilen sayıda rastgele tamsayı üretir
- **Seed Tabanlı**: Aynı seed değeri ile aynı sayı dizisini tekrar üretebilir
- **Kolay Kullanım**: Basit komut satırı arayüzü
- **Esnek Yapılandırma**: Özel parametrelerle özelleştirilebilir

## Gereksinimler

- Python 3.x

## Kurulum

1. Bu projeyi bilgisayarınıza indirin veya klonlayın.
2. Python 3.x'in yüklü olduğundan emin olun.

## Kullanım

### Temel Kullanım

Programı çalıştırmak için terminal veya komut istemcisinde aşağıdaki komutu kullanın:

```bash
python sayiüret.py
```

Program çalıştırıldığında:
1. Seed değerini girin (tam sayı)
2. Üretilecek sayı adedini belirtin
3. Program belirtilen sayıda rastgele tamsayıyı ekrana yazdıracaktır

### Örnek Çıktı

```
Seed değerini gir: 12345
Kaç sayı üretilecek?: 5

QDSNG ile üretilen sayılar:
987654321
123456789
456789012
789012345
234567890
```

## Dosya Yapısı

```
bsg2/
├── sayiüret.py          # Ana program dosyası
├── docs/
│   ├── Akış Diyagramı.txt    # Sistem akış diyagramı
│   └── Pseudocode.txt        # Pseudocode açıklaması
└── README.md            # Bu dosya
```

## Teknik Detaylar

Bu sistem, kuadratik bir formül kullanarak rastgele sayı üretir. Detaylı algoritma bilgileri ve matematiksel açıklamalar `docs/` klasöründeki dosyalarda bulunabilir.

## Güvenlik Notu

Bu sistem, kriptografik amaçlar için tasarlanmamıştır. Hassas uygulamalarda kullanılması önerilmez.

## Lisans

Bu proje açık kaynak kodludur. Detaylar için lisans dosyasına bakınız.

## Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen değişikliklerinizi test ettikten sonra pull request gönderin.