#!/usr/bin/env bash

REPO_DIR=$(dirname $(pwd)/$_)
cd $REPO_DIR
source .env/bin/activate
if [ -f requirements.txt ]
then
  pip install -r requirements.txt
fi
