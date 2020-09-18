#!/bin/bash

# Source virtual environment


if [ -z "$PROJECT_HOME" ]
then
  proj_dir=$PROJECT_HOME
else
  proj_dir=.
fi

cd $proj_dir

echo "Building Vue Static files via npm run build"
npm run build

echo "Running python manage.py collectstatic"
python manage.py collectstatic

echo "Restarting Gunicorn Server"
cd bin && ./restart-gunicorn.sh && cd ..

echo "Restarting Nginx"
sudo service nginx restart
