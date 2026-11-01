# Contributing ke santri-roadmap

Terima kasih sudah mau berkontribusi. Repo ini dijaga agar tetap ringkas, bertahap, dan berdasar kitab/rujukan yang jelas.

## Cara kontribusi

1. Fork repo ini, buat branch: `tambah-materi-bahasa-arab`, `perbaiki-fiqih-shalat`, dsb.
2. Edit file yang perlu. Satu PR untuk satu topik/roadmap agar mudah direview.
3. Jalankan cek struktur:
   ```bash
   python3 scripts/check.py
   ```
4. Buat Pull Request dengan format:
   - Judul: `[bahasa-arab] tambah materi isim isyarah`
   - Isi: apa yang diubah + rujukan (kitab, halaman, atau pendapat ustadz siapa)

## Aturan isi

1. **Bahasa Indonesia**, istilah Arab ditulis latin + arab bila perlu. Contoh: *tajwid (تجويد)*.
2. **Tadarruj (bertahap).** Jangan memasukkan materi lanjutan ke roadmap pemula.
3. **Wajib ada rujukan.** Setiap klaim fiqih/aqidah harus menyebut kitab atau ulama. Contoh: *Safinatu an-Naja, fasal shalat*.
4. **Jangan menebak URL.** Hanya cantumkan link yang kamu yakin ada (misal: quran.com, sunnah.com). Selebihnya tulis nama kitab / judul kajian tanpa link.
5. **Struktur file content** (wajib diikuti):

   ```md
   # Judul Topik

   > Ringkasan 1-2 kalimat: apa ini dan kenapa penting.

   - **Target:** ...
   - **Prasyarat:** ...
   - **Kitab/rujukan utama:** ...
   - **Estimasi:** ...

   ## Yang dipelajari

   - ...
   - ...

   ## Cara belajar

   1. ...
   2. ...

   ## Kesalahan umum

   - ...

   ## Resources

   - [@kitab@Judul Kitab — Pengarang]
   - [@artikel@Judul](https://contoh-yang-yakin-ada)
   ```

   Prefix resource yang dipakai: `@kitab@`, `@artikel@`, `@video@`, `@audio@`, `@latihan@`. Lihat contoh di `roadmaps/fondasi-santri/content/shalat.md`.

6. **README roadmap** harus memuat: untuk siapa, prasyarat, peta (checklist bernomor), estimasi waktu, dan cara setor ke guru.

## Menambah roadmap baru

Buat folder `roadmaps/<slug-baru>/` berisi:

- `README.md` (wajib: deskripsi, untuk siapa, prasyarat, tahapan, estimasi)
- `content/*.md` (minimal 5 topik, format di atas, nama file huruf-kecil-dengan-strip)

Slug memakai huruf kecil + strip. Contoh: `ushuluddin`, `dakwah-pemula`.

Lalu daftarkan di tabel `README.md` utama.

## Kode etik

Patuhi [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Perbedaan madzhab / manhaj dibahas dengan adab, dengan rujukan, tanpa mencela ulama atau sesama santri.

## Review

Maintainer akan cek:

- [ ] Struktur file benar (`scripts/check.py` lolos)
- [ ] Urutan belajar logis (tidak melompat)
- [ ] Ada rujukan yang jelas
- [ ] Bahasa rapi dan tidak menyinggung
