#!/bin/bash

(cd client && npm run build)
docker build -t hackarole -f docker/Dockerfile .
