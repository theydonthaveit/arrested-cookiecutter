import os


class Config(object):

    ALEMBIC_CONTEXT = {
        'render_as_batch': True
    }


class Dev(Config):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://{{ cookiecutter.postgres_host }}:{{ cookiecutter.postgres_port }}/{{ cookiecutter.postgres_db }}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'secret'


settings = globals()[os.environ.get('FLASK_CONFIG', 'Dev')]
