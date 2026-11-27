#!/usr/bin/env bash
# Haftalık Kanban teslim dosyalarını submission/dist/ altına kopyalar:
# Kanban_Week_NN.png ve 10. haftadan itibaren tüm görüntüler için Kanban_History_Week_10-NN.zip
# Kullanım: bash scripts/kanban_snapshot.sh NN  (veya make kanban-snapshot WEEK=NN)
set -euo pipefail

WEEK="${1:-}"
case "$WEEK" in
  1[0-4]) ;;
  *) echo "Kullanım: bash scripts/kanban_snapshot.sh <hafta 10..14>" >&2; exit 2 ;;
esac

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SHOTS="$ROOT/kanban/screenshots"
DIST="$ROOT/submission/dist"
mkdir -p "$DIST"

# Haftanın görüntüsü (.png ya da .jpg)
shot() {
  for f in "$SHOTS/Kanban_Week_$1.png" "$SHOTS/Kanban_Week_$1.jpg"; do
    if [ -f "$f" ]; then echo "$f"; return; fi
  done
}

CURRENT="$(shot "$WEEK")"
[ -n "$CURRENT" ] || { echo "HATA: kanban/screenshots/Kanban_Week_$WEEK.png bulunamadı" >&2; exit 1; }
cp "$CURRENT" "$DIST/"

ZIP="$DIST/Kanban_History_Week_10-$WEEK.zip"
rm -f "$ZIP"
for i in $(seq 10 "$WEEK"); do
  f="$(shot "$i")"
  if [ -n "$f" ]; then zip -q -j "$ZIP" "$f"; else echo "UYARI: Hafta $i görüntüsü yok" >&2; fi
done

echo "Hazır: submission/dist/$(basename "$CURRENT") ve $(basename "$ZIP")"
