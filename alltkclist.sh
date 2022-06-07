#!/bin/bash

mkdir alltkc
cd alltkc
kubectl get tkc -A -o=custom-columns="NS:.metadata.namespace,NAME:.metadata.name" > list.txt
wget https://raw.githubusercontent.com/yogeshbendre/specialtools/master/alltkckc.py -O alltkckc.py
python alltkckc.py
