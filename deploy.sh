#!/usr/bin/env bash
# Deploy situs ray-link ke /var/www/ray-link (dilayani nginx di port 80).
# Jalankan sebagai root:  bash /root/websites/ray-link/deploy.sh
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DST=/var/www/ray-link

# 1. Build ulang index.html dari build.py (opsional kalau hanya edit HTML langsung)
if [ -f "$SRC/build.py" ]; then
  python3 "$SRC/build.py"
fi

# 2. Salin berkas situs
mkdir -p "$DST"
rsync -a --delete \
  --exclude 'build.py' --exclude 'README.md' --exclude 'deploy.sh' \
  --exclude '_ref' --exclude '*.zip' --exclude 'preview.png' \
  "$SRC/" "$DST/"

chown -R www-data:www-data "$DST"
find "$DST" -type f -exec chmod 644 {} +
find "$DST" -type d -exec chmod 755 {} +

echo "Deployed to $DST"
echo "Local:  http://127.0.0.1/"
echo "Public: http://217.216.146.9/"
