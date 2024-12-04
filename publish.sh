#!/bin/bash
git add *.md
git add -u
git add static/*
git commit -am "automatic commit"

rm -rf /tmp/temp-obsidian
git clone /home/kksgandhi/Obsidian /tmp/temp-obsidian
git -C /tmp/temp-obsidian pull
# sed -i 's/\[\[\([^|]*\)|\([^]]*\)\]\]/\2 ([[\1]])/' /tmp/temp-obsidian/*.md
# perl -pie 's/\[\[([^|\]]+)\|([^\]]+\s+[^\]]+)\]\]/\2 ([[\1]])/' /tmp/temp-obsidian/*.md
# /home/kksgandhi/.cargo/bin/sd '\[\[([^|\]]+)\|([^\]]+)\]\]' '$2 ([[$1]])' /tmp/temp-obsidian/*.md

python3 post_process.py /home/kksgandhi/Obsidian /tmp/temp-obsidian

rm -rf /tmp/temp-obsidian/.neuron
neuron gen -d /tmp/temp-obsidian/

rm -rf /home/kksgandhi/Obsidian/.neuron
cp -r /tmp/temp-obsidian/.neuron /home/kksgandhi/Obsidian 
git add /home/kksgandhi/Obsidian/.neuron/*
git commit -am "automatic commit"

git push origin

git status
