import os


class Config(object):

    ALEMBIC_CONTEXT = {
        'render_as_batch': True
    }


class Dev(Config):

    DEBUG = True
    if {{cookiecutter.database_used}} == 'sqlite':
        SQLALCHEMY_DATABASE_URI = 'sqlite:////opt/code/{{cookiecutter.package_name}}.db'
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://{{ cookiecutter.postgres_host }}:{{ cookiecutter.postgres_port }}/{{ cookiecutter.postgres_db }}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'secret'


settings = globals()[os.environ.get('FLASK_CONFIG', 'Dev')]
