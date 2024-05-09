#!/bin/bash

# Crie o diretório exclude se ele não existir
mkdir -p ./exclude

# Use o comando find para obter todos os arquivos no diretório raiz e suas subpastas
find . -type f | while read file; do
  # Use grep para verificar se a primeira linha contém "#depreciado"
  if grep -q "^#depreciado" "$file"; then
    # Mova o arquivo para o diretório ./exclude
    mv "$file" ./exclude/
  fi
done
