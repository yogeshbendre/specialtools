#!/bin/bash
cd alltkc
wget https://raw.githubusercontent.com/yogeshbendre/specialtools/master/scoremerger.py -O scoremerger.py
vc=$1
wcp=$2

python scoremerger.py ./ $vc $wcp
