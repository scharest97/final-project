from flask_script import Manager
from moviebase import app, db, Star, Movie

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    downey = Star(name='Robert Downey Jr', age='53')
    chevy = Star(name='Chevy Chase', age='74')
    pratt = Star(name='Chris Pratt', age='38')
    avenger = Movie(title='Avengers', about='superheros get together', year='2012',star=downey)
    caddy = Movie(title='Caddyshack', about='the snobs vs the slobs', year='1983', star=chevy)
    galaxy = Movie(title='Guardians of the Galaxy', about='space superheros', year='2014', star=pratt)
    db.session.add(downey)
    db.session.add(chevy)
    db.session.add(pratt)
    db.session.add(avenger)
    db.session.add(caddy)
    db.session.add(galaxy)
    db.session.commit()



if __name__ == '__main__':
    manager.run()
