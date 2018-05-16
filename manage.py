from flask_script import Manager
from moviebase import app, db, Artist

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
