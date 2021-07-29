# minimal-django-prometheus
Minimal Django-Prometheus example using docker-compose.
Not tested.  Work in progress.

## How to get to this point
An easy way to start a Django app in Docker is [here](https://docs.docker.com/samples/django/).
A guide for Prometheus and AlertManager can be found in their [official documentation](https://prometheus.io/docs/introduction/overview/).
Netcat is used to fake some very silly http requests.

## Alert
Alert are firing on a Slack channel (setup a slack endpoint in ```alertmanager.yaml```) for service down and when a fake API workload is over a threshold.
 
