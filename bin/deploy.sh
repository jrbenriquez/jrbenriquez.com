#!/bin/bash

# Source virtual environment


if [ -z "$PROJECT_HOME" ]
then
  proj_dir=$PROJECT_HOME
else
  proj_dir=.
fi

cd $proj_dir

# Build Vue Static files via npm run build
npm run build
# Run python manage.py collectstatic
python manage.py collectstatic
# Restart Gunicorn Server
cd bin && ./restart-gunicorn.sh && cd ..
# Restart Nginx
sudo service nginx rest
