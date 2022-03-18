# fluentbit-example

## Build image and push to dockerhub
First: login if needed
```sh
docker login
```

Then: build docker and push
```sh
docker build -t koskuma/example-log-generator:latest -f docker/Dockerfile .
docker push koskuma/example-log-generator:latest
```

In case you want to try running
```sh
docker run --name example-log-generator koskuma/example-log-generator
```

## Docker run test database
```sh
docker run --name influxdb \
    -p 8086:8086 \
    -v influxdb:/var/lib/influxdb \
    -d influxdb
```

```sh
docker run --name elasticsearch \
    -p 9200:9200 -p 9300:9300 \
    -e "discovery.type=single-node" \
    -d docker.elastic.co/elasticsearch/elasticsearch:7.8.0
```

## Update fluent-bit deployment configurations
You have to update the IP address of the Elasticsearch and InfluxDB containers. 
In deployments/fluentbit-config.yml and deployments/fluentbit-deploy.yml: update the IP 127.0.0.1 to your IP address.
## Deploy Example Log Generator
```sh
kubectl apply -f deployments/deployment.yml
```

## Create Namespace
```sh
kubectl create namespace fluentbit-test
```

## Create RBAC for the Fluent Bit
```sh
kubectl create -f deployments/fluentbit-rbac.yml
```

## Create a ConfigMap
```sh
kubectl create -f deployments/fluentbit-config.yml
```

## Deploy Fluentbit
```sh
kubectl create -f deployments/fluentbit-deploy.yml
```
