def configure_app():
    import dotenv
    import os
    import flask

    PROJECT_ROOT = os.path.dirname("./submissions/sprint_a/__init__.py")
    print(PROJECT_ROOT)
    ENV_PATH = os.path.join(PROJECT_ROOT, ".env")
    dotenv.load_dotenv(ENV_PATH)
    app = flask.Flask(__name__)
    return app


app = configure_app()
