#!/bin/bash

mkdir chall
cd chall

git init .

git config user.name "AlpacaHack"
git config user.email "alpacahack@alpacahack.internal"

git commit --allow-empty -m 'initial commit'

# commit flag
echo "$FLAG" > flag.txt
git add flag.txt
git commit -m 'add flag'

# wipe flag
git reset --hard HEAD~1

# gc
git gc
