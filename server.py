from dotenv import load_dotenv
from flask import Flask

from APIs import blueprint as api

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True, load_dotenv=True)
