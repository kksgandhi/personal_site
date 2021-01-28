#!/bin/bash
git commit -am "automatic commit"

rm -r /tmp/temp-obsidian
git clone ./.git /tmp/temp-obsidian
neuron gen -d /tmp/temp-obsidian/

rm -r ./.neuron
cp -r /tmp/temp-obsidian/.neuron .
git add ./.neuron/*
git commit -am "automatic commit"

git push origin
