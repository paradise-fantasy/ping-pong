#!/bin/bash

# Prepare apps
mkdir -p public/apps

# Get files
aws s3 sync s3://ping-pong.komstek.no/ public/apps --delete

# Done!
