#!/usr/bin/env bash
set -euxo pipefail

ARCHIVE_PATH="all.tar.xz"

DOMAIN="fullyveganrecipes.com"

curl \
  -H "Authorization: Bearer $FX_PASSWORD" \
  https://$DOMAIN/api/download/all.tar.xz > "$ARCHIVE_PATH"

tar --verbose -xf "$ARCHIVE_PATH"
rm "$ARCHIVE_PATH"

ABOUT="$(python3 generate-about.py)"

echo "ABOUT:"
echo "$ABOUT"

curl \
  -X PUT \
  -H "Authorization: Bearer $FX_PASSWORD" \
  https://$DOMAIN/api/settings/about \
  -d "$ABOUT"
