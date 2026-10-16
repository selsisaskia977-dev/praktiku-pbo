class Buku:
    def __init__(self, judul, penulis="Tidak Diketahui", tahun_terbit=2023):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def info(self):
        print(f"Judul    : {self.judul}")
        print(f"Penulis  : {self.penulis}")
        print(f"Tahun Terbit : {self.tahun_terbit}")
        print("-" * 35)
        

buku1 = Buku("Dasar Pemrograman Python", "Andi Pratama", 2020)
buku2 = Buku("Struktur Data", "Siti Aminah", 2019)
buku3 = Buku("Basis Data", "Budi Santoso", 2021)

buku4 = Buku("Algoritma Pemrograman", tahun_terbit=2023)

buku1.info()
buku2.info()
buku3.info()
buku4.info()