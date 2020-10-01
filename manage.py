# Import db from app factory
from app import create_app, db, admin
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_admin.contrib.sqla import ModelView
from app.models import User,Post, Subscription, Comments

# Creating app instance
# app = create_app('test')
# app = create_app('development')
app = create_app('production')
app = create_app('development')


# Create manager instance 
manager = Manager(app)

# Create migrate instance
migrate = Migrate(app, db)

manager.add_command('server', Server)

manager.add_command('db', MigrateCommand)


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Subscription, db.session))
admin.add_view(ModelView(Comments, db.session))

@manager.command
def test():
    """
    Run the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)


if __name__ == '__main__':
    manager.run()