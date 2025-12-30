class QDSNG:
    def __init__(self, seed, a=37, b=11, c=23, m=2**31):
        self.a = a
        self.b = b
        self.c = c
        self.m = m
        self.state = seed

    def next_int(self):
        """Bir sonraki tamsayıyı üretir."""
        x = self.state
        self.state = (self.a * (x ** 2) + self.b * x + self.c) % self.m
        return self.state

    def next_float(self):
        """[0, 1) aralığında sayı üretir."""
        return self.next_int() / self.m


if __name__ == "__main__":
    seed = int(input("Seed değerini gir: "))
    n = int(input("Kaç sayı üretilecek?: "))

    gen = QDSNG(seed)

    print("\nQDSNG ile üretilen sayılar:")
    for _ in range(n):
        print(gen.next_int())
