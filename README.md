# ray-link — link-in-bio page

Clone of the old `linktr.ee/natsutamura` page, rebuilt as plain static HTML/CSS/JS.
No Linktree branding anywhere: no logo, no "Get your own Linktree" button, no
cookie/report/privacy footer, no external Linktree assets.

## Isi folder

| File | Fungsi |
|---|---|
| `index.html` | Seluruh situs (CSS + JS inline, ikon SVG inline) — **hasil build** |
| `build.py` | Generator `index.html` dari data di `assets/` |
| `assets/avatar.jpg` | Foto profil |
| `assets/ig-post.jpg` | Gambar kartu Instagram |
| `assets/inter-latin.woff2` | Font Inter (self-hosted, latin) |
| `assets/icon-*.svg` | Ikon Tabler untuk baris link |
| `assets/icons.json` | Path SVG ikon brand (TikTok, WhatsApp, IG, FB, YT) |
| `deploy.sh` | Copy situs ke `/var/www/ray-link` + reload nginx |

## Dashboard (tanpa edit file)

Buka **https://natsutamura.my.id/admin/** — login pakai GitHub *fine-grained token*
(Repository access: only `natsutamura/natsu-linktree`; Permissions: **Contents: Read and write**).
Di sana bisa ubah nama/bio/followers, teks About + tombol CTA, kartu unggulan,
daftar sosial, dan daftar link (tambah, hapus, urutkan, pilih ikon).

Alur simpan: dashboard commit `links.json` → GitHub Action
(`.github/workflows/build.yml`) menjalankan `build.py` → commit `index.html` baru →
GitHub Pages deploy. Total ±1 menit. Token hanya tersimpan di browser (localStorage)
dan hanya dikirim ke `api.github.com`.

## Edit konten

Pilihan paling gampang: edit langsung `index.html` (semua konten ada di bagian
`<body>`), lalu jalankan `bash deploy.sh`.

Kalau kamu lebih suka data terpusat, edit daftar di `build.py`
(`SOCIALS`, `ROWS`, `ABOUT_TEXT`, nama, bio) lalu `python3 build.py` — file
`index.html` akan dibuat ulang.

## Ganti isi

- **Nama / bio** → elemen `.name` dan `.bio` di `index.html`
- **Jumlah follower** → `.followers` (`2K followers`)
- **Baris link** → blok `<div class="card row-card">`, isi `href` + `.row__label`
- **Teks About Me** → `<p class="about__text">`
- **Tombol "Start project with me!"** → `<a class="about__cta" href="...">`
- **Kartu Instagram** → gambar `assets/ig-post.jpg` + `.media__label` / `.media__sub`
- **Warna** → variabel CSS di `:root` (`--bg`, `--line`, `--text-soft`, dst.)

## Jalankan lokal

```bash
cd /root/websites/ray-link
python3 -m http.server 8080
# buka http://127.0.0.1:8080
```

Atau pakai nginx yang sudah terpasang: `http://<ip-vps>/` (lihat catatan hosting).

## Hosting

`deploy.sh` menyalin situs ke `/var/www/ray-link`, dilayani nginx pada port 80
(config: `/etc/nginx/sites-available/ray-link`).

Catatan: IP publik VPS ini (`217.216.146.9`) adalah **IP bersama/CGNAT** — port 80
dari internet dijawab halaman gateway provider, bukan oleh VPS ini, jadi situs
belum bisa diakses publik lewat IP tersebut. Opsi yang berfungsi:

1. **GitHub Pages** — push ke repo `natsutamura/ray-link`, aktifkan Pages di
   Settings → Pages (branch `main`, folder `/`). URL: `https://natsutamura.github.io/ray-link/`
2. **Cloudflare Tunnel** — perlu domain yang diarahkan ke Cloudflare; tunnel
   langsung menuju `127.0.0.1:80` di VPS ini.
3. **Vercel / Netlify / Cloudflare Pages** — drag & drop folder ini, tanpa domain.

## Detail yang sengaja ditiru

- Background `#0A0A0A`, kartu transparan dengan border 1px `#2A2A2A`, radius 8px
- Kolom 400px, padding halaman 14px, jarak antar kartu 14px
- Avatar 96px, nama 24px/600, bio 16px/500, ikon sosial 32px dalam tap target 48px
- Baris link tinggi 64px, label 14px/500, ikon 32px di kiri, menu titik-tiga di kanan
- Kartu Instagram rasio 16:9 dengan gambar persegi di tengah + pill "Follow on Instagram"

## Tambahan (bukan dari Linktree)

- Tombol share di kanan atas (Web Share API, fallback salin link)
- Menu titik-tiga berfungsi: "Salin link" / "Bagikan"
- "More" pada About Me membuka teks penuh + tombol CTA
- Footer minimal `© <tahun> Ray`
