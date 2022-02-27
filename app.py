from flask import Flask
import os


# Env. Variables
PORT = os.environ.get('PORT') or 3000
DB_URL = os.environ.get('DB_URL') or 'mongodb://localhost:quotmia'
AUTH_KEY = os.environ.get('AUTH_KEY') or '1234567890'



app = Flask(__name__)


# Setting Routers up

# Users Router
import routers.users as users
users.setup(app= app, key= AUTH_KEY)

# Quotes Router
import routers.quotes as quotes
quotes.setup(app= app, key=AUTH_KEY)

# Writes Router
import routers.writes as writes
writes.setup(app=app, key=AUTH_KEY)

# Collections Router
import routers.collections as collections
collections.setup(app=app, key=AUTH_KEY)




if __name__ == '__main__':
    app.run(port= PORT, debug= True)
