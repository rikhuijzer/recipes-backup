#!/usr/bin/env bash
set -euxo pipefail

ARCHIVE_PATH="all.tar.xz"

curl --proto "=https" --tlsv1.2 -sSf \
  -H "Authorization: Bearer $FX_PASSWORD" \
  https://fullyveganrecipes.com/api/download/all.tar.xz > "$ARCHIVE_PATH"

tar --verbose -xf "$ARCHIVE_PATH"
