#!/bin/bash

echo "Sourcing virtual environment"
source $PROJECT_VENV_DIR/bin/activate

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
npm --prefix $PROJECT_HOME/vue_frontend run build

echo "Running python manage.py collectstatic"
yes yes | python manage.py collectstatic

echo "Restarting Gunicorn Server"
cd bin && ./restart-gunicorn.sh && cd ..

echo "Restarting Nginx"
sudo service nginx restart
