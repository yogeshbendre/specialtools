#!/bin/bash

mkdir alltkc || true
cd alltkc
kubectl get tkc -A -o=custom-columns="NS:.metadata.namespace,NAME:.metadata.name" > list.txt
wget https://raw.githubusercontent.com/yogeshbendre/specialtools/master/alltkckc.py -O alltkckc.py
python alltkckc.py
rm -rf ./-ssh
rm -rf ./-kubeconfig
ls -lrt
echo "Done"
