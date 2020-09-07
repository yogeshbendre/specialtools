# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:35:27 2020
This script will add DEV_STACK flag to TMC Installer YAML
@author: ybendre
"""
#!/usr/bin/env python3

import yaml

yamlfile = '/usr/lib/vmware-wcp/objects/PodVM-GuestCluster/70-tmc-agent-installer/tmc-agent-installer.yaml'
newyamlfile = '/usr/lib/vmware-wcp/objects/PodVM-GuestCluster/70-tmc-agent-installer/tmc-agent-installer.yaml'

yamlfile = '/root/YSB/tmc-agent-installer.yaml'
newyamlfile = yamlfile


with open(yamlfile) as f:

    docs = list(yaml.load_all(f, Loader=yaml.FullLoader))
    
    newdocs = []
    for doc in docs:
        mydoc = doc
        if doc['kind'] == 'CronJob':
            print("Found cronjob doc")
            print(mydoc["spec"]["jobTemplate"]["spec"]["template"]["spec"]["containers"][0]["env"])
            env = mydoc["spec"]["jobTemplate"]["spec"]["template"]["spec"]["containers"][0]["env"]
            isdevstack = False
            for e in env:
                if "DEV_STACK" in e['name']:
                    isdevstack = True
                    print("DEV_STACK already present.")
            if not isdevstack:
                print("Adding DEV_STACK entry.")
                mydoc["spec"]["jobTemplate"]["spec"]["template"]["spec"]["containers"][0]["env"].append({'name':'DEV_STACK','value':'"true"'})
                print(mydoc["spec"]["jobTemplate"]["spec"]["template"]["spec"]["containers"][0]["env"])
  
        newdocs.append(mydoc)
        
    with open(newyamlfile, 'w') as f:
        data = yaml.dump_all(newdocs, f, default_flow_style = False)