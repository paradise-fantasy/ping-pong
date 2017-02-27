#!/bin/bash

# Prepare apps
rm -rf public/apps
mkdir -p public/apps

# Get files
aws s3 sync s3://ping-pong.komstek.no/ public/

# Done!
