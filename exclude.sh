#!/bin/bash

mkdir -p ./docs/exclude

find ./docs -type f | while read file; do
  if grep -q "^#depreciado" "$file"; then
    mv "$file" ./docs/exclude/
  fi
done
