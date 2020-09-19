#!/bin/bash

# Source virtual environment


if [ -z "$PROJECT_HOME" ]
then
    echo "No PROJECT_HOME found. Using current directory"
    proj_dir=.
else
    echo "Setting project directory"
  proj_dir=$PROJECT_HOME
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
