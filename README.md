# QDSNG - Quadratic Discrete Stochastic Number Generator

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Proje Hakkında

QDSNG (Quadratic Discrete Stochastic Number Generator), Python ile geliştirilmiş gelişmiş bir rastgele sayı üreteci sistemidir. Kuadratik bazlı matematiksel bir yaklaşım kullanarak, deterministik ancak yüksek kaliteli rastgele sayı dizileri üretir.

Bu proje, rastgele sayı üretimi alanında akademik çalışmalar, simülasyonlar ve çeşitli uygulamalar için güvenilir bir çözüm sunmaktadır.

## ✨ Özellikler

### Temel Özellikler
- 🎲 **Kuadratik Algoritma**: Matematiksel bir yaklaşımla yüksek kaliteli rastgele sayı üretimi
- 🔄 **Deterministik Çalışma**: Aynı seed değeri ile tekrarlanabilir sonuçlar
- 🎯 **Esnek Parametre Ayarları**: Özelleştirilebilir algoritma parametreleri (a, b, c, m)
- 📊 **Tam Sayı ve Ondalık Mod**: `next_int()` ve `next_float()` metodları ile farklı veri tipleri
- ⚡ **Yüksek Performans**: Hızlı ve verimli sayı üretimi
- 🔧 **Basit API**: Kullanımı kolay ve temiz arayüz

### Test ve Doğrulama Araçları
- ✅ **Kapsamlı Test Paketi**: 8 farklı istatistiksel test içeren doğrulama sistemi
- 📈 **İstatistiksel Analizler**: Mean, Chi-Square, Runs, Autocorrelation testleri
- 🔬 **Bit Seviyesi Testler**: Monobit test ile binary düzeyde kalite kontrolü
- 🎨 **Görselleştirme**: ASCII histogram ile dağılım analizi
- 📐 **Periyot Analizi**: Üretilen dizilerin periyot özelliklerinin incelenmesi

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.x veya üzeri
- Standart Python kütüphaneleri (ek paket gerektirmez)

### Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/kullaniciadi/qdsng.git

# Proje dizinine gidin
cd qdsng
```

### Temel Kullanım

#### 1. Komut Satırı ile Kullanım

```bash
python sayiuret.py
```

Program çalıştırıldığında:
1. **Seed değeri** girin (herhangi bir tam sayı)
2. **Üretilecek sayı adedi** belirtin
3. Sonuçları ekranda görün

**Örnek Çalışma:**
```
Seed değerini gir: 123456
Kaç sayı üretilecek?: 5

QDSNG ile üretilen sayılar:
1847293857
954732889
1736284956
875629334
1928374651
```

#### 2. Python Kodu İçinde Kullanım

```python
from sayiuret import QDSNG

# Generator oluştur
gen = QDSNG(seed=123456)

# Tam sayı üret
rastgele_sayi = gen.next_int()
print(f"Rastgele tam sayı: {rastgele_sayi}")

# 0-1 arası ondalık sayı üret
rastgele_ondalik = gen.next_float()
print(f"Rastgele ondalık: {rastgele_ondalik}")

# Birden fazla sayı üret
sayilar = [gen.next_int() for _ in range(10)]
print(f"10 rastgele sayı: {sayilar}")
```

#### 3. Özel Parametrelerle Kullanım

```python
from sayiuret import QDSNG

# Özelleştirilmiş parametrelerle generator
gen = QDSNG(
    seed=42,
    a=37,      # Kuadratik katsayı
    b=11,      # Lineer katsayı  
    c=23,      # Sabit terim
    m=2**31    # Modulo değeri
)

sayi = gen.next_int()
```

## 🧪 Test ve Kalite Kontrolü

Projenin kalitesini doğrulamak için kapsamlı bir test paketi mevcuttur:

```bash
python qdsng_testleri.py
```

### Test Metrikleri

| Test Adı | Amaç | İdeal Sonuç |
|----------|------|-------------|
| **Mean Test** | Ortalama değer kontrolü | ~0.5 |
| **Chi-Square (χ²)** | Dağılım uniformluğu | χ² < 16.9 |
| **Runs Test** | Bağımsızlık analizi | Beklenen değere yakın |
| **Autocorrelation** | Ardışık korelasyon | r ≈ 0 |
| **Monobit Test** | Bit dengesi | 0/1 oranı ≈ 0.5 |
| **Histogram** | Görsel dağılım kontrolü | Dengeli çubuklar |
| **Period Test** | Periyot uzunluğu | Yüksek periyot |
| **Seed Sensitivity** | Seed hassasiyeti | Farklı sonuçlar |

### Test Çıktısı Yorumlama

- ✔ **İyi**: Test başarılı, rastgelelik kalitesi yüksek
- ⚠ **Orta**: Kabul edilebilir seviye, bazı sapmalar mevcut
- ❌ **Zayıf**: Rastgelelik kalitesi düşük, iyileştirme gerekebilir

## Dosya Yapısı

```
bsg2/
├── sayiüret.py          # Ana program dosyası
├── docs/
│   ├── Akış Diyagramı.txt    # Sistem akış diyagramı
│   └── Pseudocode.txt        # Pseudocode açıklaması
└── README.md            # Bu dosya
```

## 🎯 Kullanım Senaryoları

QDSNG aşağıdaki durumlarda kullanılabilir:

- 🎲 **Simülasyonlar**: Monte Carlo simülasyonları ve olasılık hesaplamaları
- 🎮 **Oyun Geliştirme**: Deterministik rastgele olaylar için
- 🧪 **Bilimsel Araştırma**: Tekrarlanabilir deneyler için
- 📊 **Veri Üretimi**: Test verisi ve sentetik veri oluşturma
- 🔐 **Prototipler**: Algoritma geliştirme ve test aşamaları
- 📚 **Eğitim**: Rastgele sayı üreteci algoritmalarını öğretme

> **⚠️ Önemli Not**: QDSNG kriptografik amaçlar için tasarlanmamıştır. Güvenlik gerektiren uygulamalarda (şifreleme, token üretimi vb.) kriptografik olarak güvenli rastgele sayı üreticileri kullanılmalıdır.

## 🔬 Teknik Detaylar

### API Referansı

#### `QDSNG` Sınıfı

```python
class QDSNG:
    def __init__(self, seed, a=37, b=11, c=23, m=2**31)
```

**Parametreler:**
- `seed` (int): Başlangıç değeri (herhangi bir tam sayı)
- `a` (int, opsiyonel): Kuadratik katsayı (varsayılan: 37)
- `b` (int, opsiyonel): Lineer katsayı (varsayılan: 11)
- `c` (int, opsiyonel): Sabit terim (varsayılan: 23)
- `m` (int, opsiyonel): Modulo değeri (varsayılan: 2³¹)

**Metodlar:**

##### `next_int()`
Bir sonraki rastgele tam sayıyı döndürür.

**Dönüş:** `int` - [0, m) aralığında bir tam sayı

**Örnek:**
```python
gen = QDSNG(42)
sayi = gen.next_int()  # Örn: 1234567890
```

##### `next_float()`
[0, 1) aralığında bir ondalık sayı döndürür.

**Dönüş:** `float` - [0, 1) aralığında normalize edilmiş değer

**Örnek:**
```python
gen = QDSNG(42)
sayi = gen.next_float()  # Örn: 0.5748392
```

### Performans

- **Hız**: ~1,000,000 sayı/saniye (tipik donanımda)
- **Bellek**: Minimal (sadece state bilgisi tutulur)
- **Periyot**: Yüksek (çarpışma nadir görülür)

## 📚 Dokümantasyon

Ek teknik dokümantasyon için `docs/` klasörüne bakınız:

- **Akış Diyagramı**: Algoritmanın akış şeması
- **Pseudocode**: Algoritmanın sözde kod gösterimi
- **Program Çıktıları**: Örnek test sonuçları
- **Kriptografik Analiz**: Rastgelelik kalitesi değerlendirmesi

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Projeye katkıda bulunmak için:

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

### Geliştirme Kuralları

- Kod Python PEP 8 standartlarına uygun olmalıdır
- Yeni özellikler için testler eklenmelidir
- Dokümantasyon güncel tutulmalıdır
- Commit mesajları açıklayıcı olmalıdır

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

## 📧 İletişim

Sorularınız, önerileriniz veya geri bildirimleriniz için:

- **Issues**: [GitHub Issues](https://github.com/kullaniciadi/qdsng/issues) üzerinden bildirebilirsiniz
- **Discussions**: Genel tartışmalar için GitHub Discussions kullanabilirsiniz

## 🙏 Teşekkürler

Bu projeyi kullandığınız için teşekkür ederiz! Yıldız ⭐ vermeyi unutmayın.

---

**Not**: Bu proje eğitim ve araştırma amaçlı geliştirilmiştir. Üretim ortamlarında kullanmadan önce kapsamlı testler yapılması önerilir.