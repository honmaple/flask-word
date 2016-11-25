# !/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: db_create.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-02-11 13:34:38
# *************************************************************************
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.extension import db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)


@manager.command
def runserver():
    return app.run()


@manager.command
def init_db():
    """
    Drops and re-creates the SQL schema
    """
    # db.drop_all()
    db.configure_mappers()
    db.create_all()
    db.session.commit()


@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', type=int, default=8000)
@manager.option('-w', '--workers', dest='workers', type=int, default=2)
def gunicorn(host, port, workers):
    """use gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {'bind': '{0}:{1}'.format(host, port), 'workers': workers}

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
