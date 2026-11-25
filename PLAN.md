# Rencana Kerja — Worst AI Advice: The 48-Hour Tight Line Open

## Ringkasan Tugas
Membuat program `program/v1` (tanpa jaringan) yang menulis satu baris nasihat AI terburuk ke `/output/entry.txt` (UTF-8, 1–140 karakter, bukan hanya spasi). Dinilai berpasangan oleh juri AI berdasarkan: (1) nasihat buruk yang spesifik & bisa diikuti, (2) langsung lucu pada bacaan pertama, (3) sangat padat (byte lebih kecil menang tie-break), (4) gaya suara asisten AI yang percaya diri & rapi, (5) situasi/tindakan konkret.

## Tahapan Kerja
1. **Inisialisasi & Lisensi**
   - Tambahkan berkas `LICENSE` (MIT/OSI) di root repo.
   - Siapkan struktur entrypoint `main.py` untuk runtime `python3.13`.
2. **Eksplorasi & Kurasi Kandidat One-Liner**
   - Rancang 10–15 kandidat satu baris bernada asisten AI yang sopan/percaya diri namun berakibat konyol jika diikuti.
   - Evaluasi kandidat secara berpasangan terhadap 5 kriteria juri serta efisiensi jumlah karakter dan byte.
3. **Implementasi Entrypoint (`main.py`)**
   - Tulis `main.py` untuk menulis one-liner terpilih ke `/output/entry.txt` (mendukung override direktori output untuk uji lokal).
   - Lakukan revisi iteratif minimal 2 kali pada entrypoint untuk menyempurnakan punchline dan memenuhi aturan `thinking_revised`.
4. **Pengujian & Validasi Gate Lokal**
   - Buat skrip uji `tests/validate_entry.py` untuk memeriksa: berkas ada, UTF-8 valid, panjang 1–140 karakter, 1 baris, tidak kosong, dan ukuran byte.
   - Jalankan `main.py` dan skrip validasi untuk memastikan semua syarat gate lolos.
5. **Commit Milestone & Pra-Submit**
   - Commit setiap milestone di repo ini.
   - Verifikasi kesiapan berkas submit (`LICENSE`, `main.py`, tanpa perubahan di luar aturan) sebelum pengumpulan.

## Daftar Berkas yang Akan Dibuat
- `PLAN.md` — Rencana kerja dan daftar berkas (berkas ini).
- `LICENSE` — Lisensi OSI-approved (MIT) di root repo.
- `main.py` — Entrypoint `program/v1` yang menulis one-liner final ke `/output/entry.txt`.
- `candidates.md` — Catatan eksplorasi, perbandingan berpasangan, dan seleksi kandidat one-liner.
- `tests/validate_entry.py` — Skrip validasi lokal untuk mengecek aturan gate (UTF-8, 1–140 karakter, non-whitespace, ukuran byte).
