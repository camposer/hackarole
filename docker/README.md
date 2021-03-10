# How-to Docker

In order to run the bot just build the image and start your container.

## Build
```
docker build -t hackarole -f docker/Dockerfile .
```

## Run
```
docker run -e SDM_API_ACCESS_KEY=$SDM_API_ACCESS_KEY -e SDM_API_SECRET_KEY=$SDM_API_SECRET_KEY -p 5000:5000 hackarole
```
