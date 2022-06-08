#!/bin/bash
cd alltkc
wget https://raw.githubusercontent.com/yogeshbendre/specialtools/master/kb.yaml -O kb.yaml
kclist=$(ls | grep kubeconfig | head -n 5)

for i in $kclist:
do
echo $i
kubectl --kubeconfig $i delete ns cis || true
kubectl --kubeconfig $i create ns cis || true
kubectl --kubeconfig $i -n cis apply -f kb.yaml || true
done

echo "tkc,score" > cisscore.txt
for i in $kclist:
do
echo $i
a=$(kubectl --kubeconfig $i -n cis get pods -o=custom-columns="DATA:.metadata.name" || true)
b=($a) || true
pname=${b[1]} || true
echo "Checking $pname of $i"
pdata=$(kubectl --kubeconfig $i -n cis logs $pname | tail -n 6 | grep PASS) || true
fdata=$(kubectl --kubeconfig $i -n cis logs $pname | tail -n 6 | grep FAIL) || true
wdata=$(kubectl --kubeconfig $i -n cis logs $pname | tail -n 6 | grep WARN) || true
idata=$(kubectl --kubeconfig $i -n cis logs $pname | tail -n 6 | grep INFO) || true

p1=($pdata) || true
f1=($fdata) || true
w1=($wdata) || true
i1=($idata) || true
t=$((p1 + f1 + w1 + i1)) || true
per=$((t - f1)) || true
score=$((100*per/t)) || true

echo "$i,$score" >> cisscore.txt
done


