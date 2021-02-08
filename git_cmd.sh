#!/bin/sh
python github.py $1
cd ~
cd Documents/dev
mkdir $1
cd $1
git init
touch README.md
git remote add origin git@github.com:username/$1.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin master