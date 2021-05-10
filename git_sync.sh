#!/bin/sh
git config --global credential.helper cache

#git pull
git add -A
git add *
git commit -m "$1"
git push 

