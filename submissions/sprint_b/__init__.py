def configure_app():
    import dotenv
    import os
    import flask
    from os import sys, path

    sys.path.append(
        path.dirname(path.dirname(path.abspath(__file__ + "sprint_b")))
    )
    PROJECT_ROOT = os.path.dirname("./submissions/sprint_b/__init__.py")

    ENV_PATH = os.path.join(PROJECT_ROOT, ".env")
    dotenv.load_dotenv(ENV_PATH)
    app = flask.Flask(__name__)
    return app


app = configure_app()

