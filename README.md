<p align="center">
  <h2 align="center">santri-roadmap</h2>
  <p align="center">Roadmap belajar santri yang terstruktur, bertahap, dan berbasis kitab kuning — dari fondasi hingga alim.</p>
  <p align="center">
    <img src="https://img.shields.io/badge/%E2%9C%A8-Roadmaps-0a5c36.svg?style=flat&colorA=0a5c36" alt="roadmaps" />
    <img src="https://img.shields.io/badge/%F0%9F%93%9A-Kitab_Kuning-eab308.svg?style=flat&colorA=eab308" alt="kitab kuning" />
    <img src="https://img.shields.io/badge/Bahasa-Indonesia-red.svg" alt="bahasa indonesia" />
  </p>
</p>

> Terinspirasi oleh [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) (roadmap.sh), tapi untuk santri: panduan belajar agama yang jelas alurnya — apa yang dipelajari dulu, apa berikutnya, sampai mana targetnya.

## Daftar Roadmap

| # | Roadmap | Untuk siapa | Isi singkat |
|---|---------|-------------|-------------|
| 01 | [Fondasi Santri](roadmaps/fondasi-santri/) | Santri baru / pemula, 0–1 tahun | Niat & adab, aqidah dasar, thaharah, shalat, puasa, baca Qur'an, dzikir harian, sirah |
| 02 | [Tahfidz Qur'an](roadmaps/tahfidz-quran/) | Penghafal Qur'an | Tahsin, tajwid, ziyadah, muraja'ah, tasmi', sanad |
| 03 | [Bahasa Arab](roadmaps/bahasa-arab/) | Semua santri (alat utama) | Hijaiyah, kosakata, nahwu, sharaf, i'rab, muhadatsah, qira'ah, kitabah |
| 04 | [Kitab Kuning](roadmaps/kitab-kuning/) | Santri menengah–lanjut | Cara baca kitab gundul, nahwu–sharaf lanjutan, fiqih, ushul fiqih, hadits, tafsir, tauhid, tasawuf |
| 05 | [Fiqih Ibadah](roadmaps/fiqih-ibadah/) | Semua santri | Thaharah–shalat–puasa–zakat–haji, muamalah, munakahat, waris, fiqih kontemporer |
| 06 | [Akhlak & Tasawuf](roadmaps/akhlak-tasawuf/) | Semua santri | Tazkiyatun nafs, ikhlas–sabar–syukur, adab guru & orang tua, ukhuwah, dzikir |
| 07 | [Santri Digital](roadmaps/santri-digital/) | Santri melek teknologi | Literasi digital, office, desain dakwah, video dakwah, coding dasar, keamanan digital |

Juga ada:

- [Best Practices — Adab Menuntut Ilmu](best-practices/adab-menuntut-ilmu.md)
- [Questions — Uji pemahaman](questions/) — kumpulan soal per roadmap untuk menguji diri

## Cara pakai

1. Pilih satu roadmap sesuai posisimu. Jangan loncat. Contoh: baru masuk pesantren → mulai dari `fondasi-santri`.
2. Buka `README.md` di folder roadmap itu. Ikuti urutan tahap 0 → 1 → 2 → ...
3. Setiap topik punya file di `content/`. Contoh: `roadmaps/fondasi-santri/content/shalat.md`. Baca target & rujukan kitabnya.
4. Centang yang sudah selesai. Lanjut ke topik berikutnya. Satu roadmap = 6–24 bulan tergantung intensitas.
5. Kalau stuck, buka `best-practices/adab-menuntut-ilmu.md`.

```
roadmaps/<roadmap-slug>/README.md      <- peta & urutan belajar (mulai dari sini)
roadmaps/<roadmap-slug>/content/<topik>.md  <- materi per topik: target, kitab, cara belajar
```

Contoh:

```
roadmaps/fondasi-santri/content/shalat.md
roadmaps/bahasa-arab/content/nahwu-dasar.md
roadmaps/tahfidz-quran/content/murajaah.md
```

Setiap file content strukturnya sama:

```md
# Judul Topik

> Ringkasan satu paragraf.

- Target: ...
- Kitab/rujukan: ...
- Cara belajar: ...
- Kesalahan umum: ...

## Resources
- kitab / artikel / video
```

## Prinsip

1. **Adab sebelum ilmu.** Semua roadmap mulai dari niat & adab.
2. **Talaqqi ke guru.** Repo ini bukan pengganti guru & pesantren. Semua materi wajib disetorkan / ditashih ke ustadz.
3. **Bertahap (tadarruj).** Jangan belajar Alfiyah sebelum Jurumiyah. Jangan Fathul Mu'in sebelum Safinah.
4. **Bahasa Indonesia.** Istilah Arab tetap dipakai, tapi penjelasan berbahasa Indonesia.
5. **Terbuka.** Silakan koreksi via Issues / Pull Request. Lihat [CONTRIBUTING.md](CONTRIBUTING.md).

## Struktur repo

```
santri-roadmap/
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── roadmaps/
│   ├── fondasi-santri/README.md + content/*.md
│   ├── tahfidz-quran/README.md + content/*.md
│   ├── bahasa-arab/README.md + content/*.md
│   ├── kitab-kuning/README.md + content/*.md
│   ├── fiqih-ibadah/README.md + content/*.md
│   ├── akhlak-tasawuf/README.md + content/*.md
│   └── santri-digital/README.md + content/*.md
├── best-practices/
│   └── adab-menuntut-ilmu.md
├── questions/
│   ├── fondasi-santri.md
│   ├── tahfidz-quran.md
│   ├── bahasa-arab.md
│   ├── kitab-kuning.md
│   ├── fiqih-ibadah.md
│   ├── akhlak-tasawuf.md
│   └── santri-digital.md
└── scripts/
    └── check.py  <- validasi struktur & link antar file
```

Berbeda dengan repo asli `developer-roadmap` yang file content-nya bernama `<slug>@<node-id>.md` untuk sinkronisasi ke database roadmap.sh, repo ini memakai nama file bersih (`shalat.md`, bukan `shalat@xxxx.md`) karena mandiri dan dibaca langsung di GitHub.

## Kontribusi

Lihat [CONTRIBUTING.md](CONTRIBUTING.md). Intinya:

- Tambah materi ke roadmap yang ada
- Buat roadmap baru (misal: ushuluddin, dakwah, tahsin khusus, dsb)
- Perbaiki isi yang keliru (dengan rujukan kitab/ulama)
- Diskusi via Issues

## Terima kasih

Untuk para kiai, ustadz, dan santri yang menjaga ilmu. Terinspirasi oleh komunitas [roadmap.sh](https://roadmap.sh).

## Lisensi

[MIT](LICENSE) — bebas dipakai pesantren, madrasah, TPQ, dan komunitas. Cantumkan sumber.
