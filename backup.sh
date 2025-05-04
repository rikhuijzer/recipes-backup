#!/usr/bin/env bash
set -euxo pipefail

DOMAIN="fullyveganrecipes.com"

cleanup() {
  rm -rf files/ posts/ settings/
}

download() {
  ARCHIVE_PATH="all.tar.xz"
  curl --proto "=https" -sSf \
    -H "Authorization: Bearer $FX_PASSWORD" \
    https://$DOMAIN/api/download/all.tar.xz > "$ARCHIVE_PATH"

  tar --verbose -xf "$ARCHIVE_PATH"
  rm "$ARCHIVE_PATH"
}

commit() {
  if [ -n "$(git status --porcelain)" ]; then
    git config --global user.email "$GITHUB_ACTOR@users.noreply.github.com"
    git config --global user.name "$GITHUB_ACTOR"

    git add .
    git commit -m '[bot] backup'
    git push
  fi
}

update_about() {
  ABOUT="$(python3 generate-about.py)"
  curl -sSf \
    -X PUT \
    -H "Authorization: Bearer $FX_PASSWORD" \
    https://$DOMAIN/api/settings/about \
    -d "$ABOUT"
}

if [[ "$1" == "cleanup" ]]; then
  cleanup
elif [[ "$1" == "download" ]]; then
  download
elif [[ "$1" == "commit" ]]; then
  commit
elif [[ "$1" == "update-about" ]]; then
  update_about
fi
