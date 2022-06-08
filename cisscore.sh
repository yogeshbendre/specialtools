#!/bin/bash
cd alltkc
wget https://raw.githubusercontent.com/yogeshbendre/specialtools/master/kb.yaml -O kb.yaml
kclist=$(ls | grep kubeconfig)

for i in $kclist:
do
kubectl --kubeconfig $i create ns cis || true
kubectl --kubeconfig $i -n cis apply -f kb.yaml || true
done

echo "tkc,score" > cisscore.txt
for i in $kclist:
do
a=$(kubectl --kubeconfig $i -n cis get pods -o=custom-columns="DATA:.metadata.name" || true)
b=($a)
pname=${b[1]}
pdata=$(kubectl --kubeconfig tkgns1-c1-kubeconfig -n cis logs $pname | tail -n 6 | grep PASS)
fdata=$(kubectl --kubeconfig tkgns1-c1-kubeconfig -n cis logs $pname | tail -n 6 | grep FAIL)
wdata=$(kubectl --kubeconfig tkgns1-c1-kubeconfig -n cis logs $pname | tail -n 6 | grep WARN)
idata=$(kubectl --kubeconfig tkgns1-c1-kubeconfig -n cis logs $pname | tail -n 6 | grep INFO)

p1=($pdata)
f1=($fdata)
w1=($wdata)
i1=($idata)
t=$((p1 + f1 + w1 + i1))
per=$((t - f1))
score=$((100*per/t))

echo "$i,$score" >> cisscore.txt
done


