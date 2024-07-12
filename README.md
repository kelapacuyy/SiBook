# SiBook: Sistem Informasi Toko Buku Online 

Kelompok 3 Analisis dan Desain Sistem P2

## Deskripsi:
SiBook adalah toko buku online yang dirancang seperti situs e-commerce, khusus untuk membeli buku. Fitur-fitur utamanya meliputi:
- Pendaftaran dan login
- Halaman utama dan katalog buku
- Detail buku
- Pencarian buku
- Keranjang belanja
- Checkout dan pembayaran
- Pengecekan status pesanan.


## Anggota:
|  | Nama  | NIM | Role |
| - | ------------- | ------------- | -
| 1 | Dhianita Shafa  | G6401211016 | PM, System Analyst |
| 2 | Eva Fitriyaningsih  | G6401211048  | UI/UX |
| 3 | Annisa Nur Rahmadhani  | G6401211089 |  Front End Developer|
| 4 | Muhammad Ghifar Azka Nurhadi | G6401211108 | Back End Developer |

## Cara menjalankan:

1. Clone repository ke local
```
cd SiBook
```

2. Buat virtual environment
```
python -m venv venv
```

3. AKtifkan virtual environment
```
source venv/Scripts/activate
```

4. Install dependency
```
pip3 install -r sibook-project/requirements.txt
```

5. Jalankan server Django
```
python sibook-project/manage.py runserver
```

6. Pergi ke localhost port 8000 atau http://127.0.0.1:8000/
