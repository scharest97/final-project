# Movie Base that Is Not IMDB (FINAL PROJECT)

This final project is a **movie database** of action movies. The tables in the database are Movie and Actors/Actress, which will be called stars in this database.

More specifically, Movie will have columns such as Title, About, Year, and Star. The Star table will have columns such as Name and Age.

## AND YOU MAY ASK YOURSELF, HOW DO I WORK THIS?

For reference: the movies table will look like this with data already in the tables:

Title | About | Year | Star
------------ | -------------
The Avengers| Superheroes finally get together | 2012 | Robert Downey Jr
Caddyshack| The Snobs Vs The Slobs| 1980 | Chevy Chase
Guardians of the Galaxy| Space Pirate Fights Space God | 2014 | Chris Pratt

The Star Table will look like this:

Name | Age
------------ | -------------
Robert Downey Jr.| 53
Chevy Chase| 74
Chris Pratt| 38


This is a database, so you can add movies to the table!

# BUT FIRST...

In order to have this work in the first place, you need to initialize the database with the following code below from a user standpoint:


To activate the virtual environment:

    $ source venv/bin/activate

To run the deployment server (use '-d' to activate the debugger and reloader):

    $ python manage.py runserver -d
