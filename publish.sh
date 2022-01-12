#!/bin/bash
git add *.md
git add -u
git commit -am "automatic commit"

rm -rf /tmp/temp-obsidian
git clone ./.git /tmp/temp-obsidian
# sed -i 's/\[\[\([^|]*\)|\([^]]*\)\]\]/\2 ([[\1]])/' /tmp/temp-obsidian/*.md
# perl -pie 's/\[\[([^|\]]+)\|([^\]]+\s+[^\]]+)\]\]/\2 ([[\1]])/' /tmp/temp-obsidian/*.md
# /home/kksgandhi/.cargo/bin/sd '\[\[([^|\]]+)\|([^\]]+)\]\]' '$2 ([[$1]])' /tmp/temp-obsidian/*.md

python3 post_process.py . /tmp/temp-obsidian

rm -rf /tmp/temp-obsidian/.neuron
neuron gen -d /tmp/temp-obsidian/

rm -rf ./.neuron
cp -r /tmp/temp-obsidian/.neuron .
git add ./.neuron/*
git commit -am "automatic commit"

git push origin

git status
