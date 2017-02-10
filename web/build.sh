#!/bin/bash

# Set build environment
mv .env tmp.env
mv production.env .env

npm run build

# Revert environment
mv .env production.env
mv tmp.env .env

# Push files to AWS S3
aws s3 sync build/ s3://ping-pong.komstek.no/apps/game --delete

# Done!
