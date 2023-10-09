import sqlalchemy
from sqlalchemy.orm import sessionmaker
## @package db
#
# Responsible for manage the database.

## Connect to the database and create an Engine object used to identify the database.
# @param user A String with the database username.
# @param password A String with the database password.
# @param db A String with the database name.
# @param host A String with the database IP address.
# @param port The number of the port.
def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    return con


# engine = connect("postgres", "", "atletec-softec")
# engine = connect("postgres", "admin", "atletec-softec")
engine = sqlalchemy.create_engine('sqlite:///bufete-sw.db')

Session = sessionmaker(bind=engine)
## @var session
# Responsible to handle with the database directly.
session = Session()
