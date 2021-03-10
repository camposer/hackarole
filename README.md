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

Open in your browser: http://localhost:5000

## Test API

In case you want to test directly the API:
```
curl -X POST -H "Content-Type: application/json" -d '[{ "email": "user5@example.com", "first_name": "User5", "last_name": "Test", "resources_to_grant": [ { "name": "rodo-eks-db", "type": "POSTGRES" }], "resources_to_revoke": [] }]' http://localhost:5000/api/v1/user-resources
```


