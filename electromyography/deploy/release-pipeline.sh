USERNAME=lyscm

export CR_PAT=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
echo $CR_PAT | docker login ghcr.io -u $USERNAME --password-stdin

CONTAINER_NAME=electromyography
TAG=ghcr.io/$USERNAME/$CONTAINER_NAME:arm32v7

docker buildx build --platform linux/arm/v7 --no-cache -t $TAG .. #--push

#CONTAINER_NAME=electromyography
#IMAGE_NAME=ghcr.io/$USERNAME/$CONTAINER_NAME:arm32v7
#
#docker stop $CONTAINER_NAME
#docker rm $CONTAINER_NAME
#
#docker rm $CONTAINER_NAME
#
#docker run \
#    -d \
#    --name $CONTAINER_NAME \
#    --net=host \
#    --privileged \
#    --restart=unless-stopped \
#    $IMAGE_NAME