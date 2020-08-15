#!/bin/bash
mkdir LIAgent
cd LIAGENT
curl -k -X GET $LI_AGENT_URL --output LIAgent.rpm
chmod 777 LIAgent.rpm
SERVERHOST=$LI_HOST rpm -i LIAgent.rpm
echo '[common|filelog]' >> /var/lib/loginsight-agent/liagent.ini
echo "tags = {\"target\":\"tkg\",\"vcenter\":\"$VCENTER\",\"wcp_cluster\":\"$WCP_CLUSTER\",\"wcp_namespace\":\"$WCP_NAMESPACE\",\"tkg_cluster\":\"$TKG_CLUSTER\",\"tkg_node_name\":\"$MY_NODE_NAME\", \"pod_name\":\"$MY_POD_NAME\"}" >> /var/lib/loginsight-agent/liagent.ini
echo 'parser=auto' >> /var/lib/loginsight-agent/liagent.ini 
/etc/init.d/liagentd start 
while true
do echo $MY_NODE_NAME; sleep 60; 
done