import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)
        
    @app.route('/hello')
    def hello():
        return 'Hello World'

    from xfil import xfiltrate
    app.register_blueprint(xfiltrate.bp)
    return app