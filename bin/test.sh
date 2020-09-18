#!/bin/bash

if [ -z "$PROJECT_HOME" ]
then
  proj_dir=$PROJECT_HOME
else
  proj_dir=.
fi

cd $proj_dir
./restart-gunicorn.sh


