#!/bin/bash

mkdir alltkc
cd alltkc
kubectl get tkc -A -o=custom-columns="NS:.metadata.namespace,NAME:.metadata.name" > mytkclist.txt
python alltkckc.py
