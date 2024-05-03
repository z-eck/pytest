#!/bin/bash

DIR_PATH="libs"

FILES=""

while IFS= read -r -d '' file
do
  file=${file#"$DIR_PATH/"}

  file=${file//\//.}

  FILES+="$file "
done < <(find "$DIR_PATH" -type f -print0)

echo "$FILES"
