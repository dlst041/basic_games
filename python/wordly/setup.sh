#!/bin/bash

# python calls to words.py script to create initial lists of words for main.py
echo "Generating Word Lists..."

python words/words.py -c 30 -d easy
python words/words.py -c 30 -d medium
python words/words.py -c 30 -d hard
echo "Word Lists Generated"