# Flask Demo Project

This demo shows my favorite folder structure of a small flask project.

# Development

start debug server:

	export FLASK_ENV=development
	export FLASK_APP=flask_demo
	export FLASK_DEMO_SETTINGS_FILE=`pwd`/local_settings.py
	python3 -m flask run -h 0.0.0.0 -p 8080

run command

	export FLASK_ENV=development
	export FLASK_APP=flask_demo
	export FLASK_DEMO_SETTINGS_FILE=`pwd`/local_settings.py
	python3 -m flask create --project X Y


# Deployment

	export FLASK_ENV=production
	export FLASK_APP=flask_demo
	export FLASK_DEMO_SETTINGS_FILE=/path/to/production_settings.py
	python3 -m flask run -h 0.0.0.0 -p 80
