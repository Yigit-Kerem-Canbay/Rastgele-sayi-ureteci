from sayiuret import QDSNG  # QDSNG sınıfını sayiuret.py dosyasından alıyoruz

M = 2**31  # Mod değeri (QDSNG ile aynı olmalı)


def generate_numbers(seed=123456, count=10000):
    """
    QDSNG kullanarak 'count' adet sayı üretir ve liste olarak döndürür.
    """
    gen = QDSNG(seed)
    numbers = []
    for _ in range(count):
        numbers.append(gen.next_int())
    return numbers


# ============================
# 1) MEAN (ORTALAMA) TESTİ
# ============================
def mean_test(numbers):
    normalized = [x / M for x in numbers]
    mean_val = sum(normalized) / len(normalized)

    expected = 0.5
    difference = abs(mean_val - expected)

    print("===== 1) MEAN (ORTALAMA) TESTİ =====")
    print(f"Beklenen Ortalama : {expected}")
    print(f"Bizim Ortalama    : {mean_val}")
    print(f"Fark              : {difference}")

    if difference < 0.02:
        print("Sonuç: ✔ Ortalama değeri iyi, dağılım dengeli görünüyor.\n")
    elif difference < 0.05:
        print("Sonuç: ⚠ Orta seviye, biraz sapma var ama başlangıç için kabul edilebilir olabilir.\n")
    else:
        print("Sonuç: ❌ Zayıf, rastgelelik kalitesi düşük görünüyor.\n")


# ============================
# 2) Kİ-KARE (χ²) TESTİ
# ============================
def chi_square_test(numbers, bin_count=10):
    normalized = [x / M for x in numbers]

    bins = [0] * bin_count
    for n in normalized:
        index = int(n * bin_count)
        if index == bin_count:
            index = bin_count - 1
        bins[index] += 1

    total = len(normalized)
    expected = total / bin_count

    chi = 0
    for observed in bins:
        chi += (observed - expected) ** 2 / expected

    # 10 bin → serbestlik derecesi 9 → kritik değer ~16.9 (α=0.05)
    critical_value = 16.9

    print("===== 2) Kİ-KARE (χ²) TESTİ =====")
    print("Aralık başına beklenen :", expected)
    print("Gerçek Bin değerleri   :", bins)
    print("Hesaplanan χ²          :", chi)
    print("Kritik değer (α=0.05)  :", critical_value)

    if chi < critical_value:
        print("Sonuç: ✔ İyi. Dağılım istatistiksel olarak kabul edilebilir görünüyor.\n")
    else:
        print("Sonuç: ❌ Kötü. Sayılar eşit dağılmıyor, rastgelelik zayıf olabilir.\n")

    return bins  # Histogram için de kullanabiliriz


# ============================
# 3) RUNS TEST (BAĞIMSIZLIK)
# ============================
def runs_test(numbers):
    normalized = [x / M for x in numbers]
    mean_val = sum(normalized) / len(normalized)

    sequence = ['1' if x >= mean_val else '0' for x in normalized]

    runs = 1
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            runs += 1

    n1 = sequence.count('1')
    n0 = sequence.count('0')

    print("===== 3) RUNS TESTİ (BAĞIMSIZLIK) =====")
    print(f"Toplam sayı        : {len(numbers)}")
    print(f"Ortalama üstü (1)  : {n1}")
    print(f"Ortalama altı (0)  : {n0}")

    if n1 == 0 or n0 == 0:
        print("Sonuç: ❌ Test yapılamadı. Veriler yeterince çeşitli değil (hepsi üstte ya da altta).\n")
        return

    expected_runs = 1 + (2 * n1 * n0) / (n1 + n0)
    diff = abs(runs - expected_runs)

    print(f"Beklenen Run Sayısı: {expected_runs}")
    print(f"Gerçek Run Sayısı  : {runs}")
    print(f"Fark               : {diff}")

    if diff < expected_runs * 0.1:
        print("Sonuç: ✔ İyi. Bağımsızlık kabul edilebilir görünüyor.\n")
    elif diff < expected_runs * 0.25:
        print("Sonuç: ⚠ Orta seviye, biraz sapma var.\n")
    else:
        print("Sonuç: ❌ Kötü. Sayılar bağımsız görünmüyor.\n")


# ============================
# 4) HISTOGRAM (METİN TABANLI)
# ============================
def histogram(numbers, bin_count=10):
    """
    0–1 aralığını bin_count dilime bölüp,
    her dilime düşen sayı adedini ASCII çubuk grafik olarak gösterir.
    """
    normalized = [x / M for x in numbers]
    bins = [0] * bin_count

    for n in normalized:
        index = int(n * bin_count)
        if index == bin_count:
            index = bin_count - 1
        bins[index] += 1

    max_count = max(bins)
    scale = 50 / max_count if max_count > 0 else 1  # Maksimum çubuk uzunluğu 50 karakter

    print("===== 4) HISTOGRAM (0-1 ARASI DAĞILIM) =====")
    for i, count in enumerate(bins):
        bar = "#" * int(count * scale)
        start = i / bin_count
        end = (i + 1) / bin_count
        print(f"[{start:0.1f}, {end:0.1f}): {count:5d} | {bar}")
    print("Not: Çubuklar birbirine yakınsa dağılım daha dengelidir.\n")


# ============================
# 5) AUTOCORRELATION (LAG-1)
# ============================
def autocorrelation_test(numbers):
    """
    Lag-1 autocorrelation (ardışık elemanlar arası korelasyon).
    Bağımsız sayılar için bu değerin 0'a yakın olması beklenir.
    """
    normalized = [x / M for x in numbers]
    n = len(normalized)

    x = normalized[:-1]
    y = normalized[1:]

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    den_x = sum((xi - mean_x) ** 2 for xi in x)
    den_y = sum((yi - mean_y) ** 2 for yi in y)

    if den_x == 0 or den_y == 0:
        print("===== 5) AUTOCORRELATION TESTİ =====")
        print("Varyans sıfır olduğu için korelasyon hesaplanamadı.\n")
        return

    r = num / (den_x ** 0.5 * den_y ** 0.5)

    print("===== 5) AUTOCORRELATION TESTİ (lag-1) =====")
    print(f"Hesaplanan korelasyon r  : {r}")
    print("Beklenen (ideal) değer   : 0 (bağımsızlık varsayımı)")

    abs_r = abs(r)
    if abs_r < 0.05:
        print("Sonuç: ✔ Çok iyi. Ardışık sayılar arasında anlamlı bir ilişki görünmüyor.\n")
    elif abs_r < 0.15:
        print("Sonuç: ⚠ Orta seviye. Bir miktar ilişki olabilir.\n")
    else:
        print("Sonuç: ❌ Kötü. Ardışık sayılar arasında güçlü ilişki var, rastgelelik zayıf olabilir.\n")


# ============================
# 6) MONOBIT TEST (BIT SEVİYESİ)
# ============================
def monobit_test(numbers, bit_length=31):
    """
    Üretilen sayıları ikili (binary) forma çevirip,
    0 ve 1 bitlerinin sayısını karşılaştırır.
    """
    ones = 0
    zeros = 0

    for num in numbers:
        # bit_length kadar bite genişlet, örn: 31 bit
        bits = format(num, f"0{bit_length}b")
        ones += bits.count("1")
        zeros += bits.count("0")

    total_bits = ones + zeros
    ratio_ones = ones / total_bits
    ratio_zeros = zeros / total_bits
    diff = abs(ratio_ones - 0.5)

    print("===== 6) MONOBIT TEST (BIT SEVİYESİ) =====")
    print(f"Toplam bit sayısı : {total_bits}")
    print(f'1 sayısı          : {ones}  ({ratio_ones:.4f})')
    print(f'0 sayısı          : {zeros}  ({ratio_zeros:.4f})')
    print(f"Beklenen oran     : 0.5")
    print(f"1 oranı farkı     : {diff}")

    if diff < 0.02:
        print("Sonuç: ✔ İyi. Bit seviyesinde 0 ve 1 dengeli görünüyor.\n")
    elif diff < 0.05:
        print("Sonuç: ⚠ Orta seviye. Bir miktar dengesizlik var.\n")
    else:
        print("Sonuç: ❌ Kötü. Bit seviyesinde dengesizlik güçlü, rastgelelik zayıf.\n")


# ============================
# 7) PERİYOT İÇİN BASİT KONTROL
# ============================
def period_sample_test(seed=123456, max_steps=50000):
    """
    Tam periyot hesaplamak zor; bunun yerine:
    - max_steps adım boyunca üretilen state'ler takip edilir.
    - Aynı state tekrar görülürse, örnek periyot uzunluğu raporlanır.
    """
    gen = QDSNG(seed)
    seen = {}
    state = gen.state

    for i in range(max_steps):
        if state in seen:
            first_index = seen[state]
            period_length = i - first_index
            print("===== 7) PERİYOT ÖRNEK TESTİ =====")
            print(f"Seed             : {seed}")
            print(f"İlk tekrar index : {i}")
            print(f"Örnek periyot    : {period_length}")
            print("Not: Bu tam periyot olmayabilir, sadece örnek bir tekrar noktasıdır.\n")
            return
        else:
            seen[state] = i
            state = gen.next_int()

    print("===== 7) PERİYOT ÖRNEK TESTİ =====")
    print(f"Seed: {seed}")
    print(f"{max_steps} adım boyunca tekrar eden state gözlenmedi.")
    print("Not: Bu, periyot en az bu kadar uzun olabilir demektir ama tam periyodu garanti etmez.\n")


# ============================
# 8) SEED SENSITIVITY TEST
# ============================
def seed_sensitivity_test(seeds=(10, 11, 12), sample_len=10):
    """
    Farklı seed değerleri için ilk 'sample_len' sayıyı üretip
    yan yana karşılaştırır.
    """
    print("===== 8) SEED SENSITIVITY TEST =====")
    print(f"Kullanılan seed değerleri: {seeds}")
    print(f"Her seed için ilk {sample_len} sayı gösteriliyor:\n")

    sequences = []
    for s in seeds:
        gen = QDSNG(s)
        seq = [gen.next_int() for _ in range(sample_len)]
        sequences.append((s, seq))

    # Yazdır
    for s, seq in sequences:
        print(f"Seed = {s} --> {seq}")

    print("\nYorum:")
    print("- Farklı seed'ler için çıkan diziler birbirinden yeterince farklı olmalıdır.")
    print("- Diziler çok benziyorsa, seed hassasiyeti zayıf demektir.\n")


# ============================
# ANA ÇALIŞTIRMA BLOĞU
# ============================
if __name__ == "__main__":
    seed = 123456
    count = 10000  # İstatistik testleri için üretilecek sayı adedi

    print(f"QDSNG ile {count} sayı üretiliyor...\n")
    nums = generate_numbers(seed, count)

    mean_test(nums)
    chi_bins = chi_square_test(nums, bin_count=10)
    runs_test(nums)
    histogram(nums, bin_count=10)
    autocorrelation_test(nums)
    monobit_test(nums, bit_length=31)
    period_sample_test(seed=seed, max_steps=50000)
    seed_sensitivity_test(seeds=(10, 11, 12), sample_len=10)
