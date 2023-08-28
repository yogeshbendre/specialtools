#!/bin/bash
echo "Creating tasks"
curl -X POST -d "{\"task\": \"Task 1\"}" tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/task
sleep 2s
curl -X POST -d "{\"task\": \"Task 2\"}" tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/task
sleep 2s
curl -X POST -d "{\"task\": \"Task 3\"}" tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/task
sleep 2s
curl -X POST -d "{\"task\": \"Task 4\"}" tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/task
sleep 2s
curl -X POST -d "{\"task\": \"Task 5\"}" tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/task
sleep 2s
echo "Read all the tasks"
curl tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/tasks
echo "sleeping for 10s"
sleep 10s
echo "Deleting tasks"
curl -X POST tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/tasks/delete
sleep 2s
echo "Check if tasks deleted"
curl tasksapp-svc.workload-mongodbwebapptransactions.svc.cluster.local:8080/tasks
echo "Done DB Ops"
