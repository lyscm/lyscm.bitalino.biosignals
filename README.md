# BITALINO BIOSIGNALS - REPOSITORY <h1> 

[![electromyography - CI](https://github.com/lyscm/lyscm.bitalino.biosignals/actions/workflows/electromyography-CI.yml/badge.svg?branch=master)](https://github.com/lyscm/lyscm.bitalino.biosignals/actions/workflows/electromyography-CI.yml)

## Initiate package(s): <h2> 

Set parameters:

```bash
OWNER=lyscm
CONTAINER_NAME=lyscm.bitalino-emg-app
TAG=ghcr.io/lyscm/lyscm.bitalino.biosignals/electromyography
```
Remove any existing container:

```bash
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker pull $TAG
```

Run container:

```bash
docker run \
    -d \
    --name $CONTAINER_NAME \
    --net=host \
    --privileged \
    --restart unless-stopped \
    $TAG
```
