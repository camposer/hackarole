# Hackarole

Simple app that uses the SDM API to update user resources

## Build
```
./build.sh
```

## Run
```
docker run -e SDM_API_ACCESS_KEY=$SDM_API_ACCESS_KEY -e SDM_API_SECRET_KEY=$SDM_API_SECRET_KEY -p 5000:5000 hackarole
```

