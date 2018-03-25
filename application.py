import flask
from flask_bootstrap import Bootstrap
import os
 
def create_app():
    application= flask.Flask(__name__)
    Bootstrap(application)
    return application

application = create_app()

# Only enable Flask debugging if an env var is set to true
application.debug = os.environ.get('FLASK_DEBUG') in ['true', 'True']

# Get application version from env
application_version = os.environ.get('APP_VERSION')

# Get cool new feature flag from env
enable_cool_new_feature = os.environ.get('ENABLE_COOL_NEW_FEATURE') in ['true', 'True']


@application.route('/')
def index():
    return flask.render_template('index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0')
