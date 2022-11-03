#!/bin/bash
cd alltkc
kclist=$(ls | grep kubeconfig)

for i in $kclist
do
echo $i
kubectl --kubeconfig $i delete ns wavefront-collector || true
done
