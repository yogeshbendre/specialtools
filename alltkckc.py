#Python

import subprocess

alltkc = ""
with open("list.txt", "r") as fp:
  alltkc=fp.read()

alltkc=alltkc.split("\n")

for s in alltkc[1:]:
  a = s.split(' ')
  ns = a[0]
  tkc = a[-1]
  print(tkc)
  cmd = "kubectl get secret -n "+ns+" "+tkc+"-kubeconfig -o jsonpath='{.data.value}' | base64 -d > "+tkc+"-kubeconfig"
  proc = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  my_status, stderr_value = proc.communicate()
  my_status = my_status.decode("utf-8").strip()
  
  #kubectl get secret -n $ns $c-ssh -o jsonpath='{.data.ssh-privatekey}' | base64 -d > $c-ssh
  cmd = "kubectl get secret -n "+ns+" "+tkc+"-ssh -o jsonpath='{.data.ssh-privatekey}' | base64 -d > "+tkc+"-ssh"
  proc = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  my_status, stderr_value = proc.communicate()
  my_status = my_status.decode("utf-8").strip()

