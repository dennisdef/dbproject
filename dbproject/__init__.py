from flask import Flask
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)

app.config["MYSQL_USER"] = ''
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = ''
app.config["MYSQL_HOST"] = ''
app.config["SECRET_KEY"] = '\xfc\x1a\x1b\x91G\x97E\xceb\xaa\x15\xa8u\x86\xaf\x13\x9fm\x1e\xbb\x85\t' ## secret key for sessions (signed cookies). Flask uses it to protect the contents of the user session against tampering.
app.config["WTF_CSRF_SECRET_KEY"] = '\xfc\x1a\x1b\x91G\x97E\xceb\xaa\x15\xa8u\x86\xaf\x13\x9fm\x1e\xbb\x85\t' ## token for csrf protection of forms.
## secret keys can be generated by secrets.token_hex()

## initialize database connection object
db = MySQL(app)
csrf = CSRFProtect(app)
## routes must be imported after the app object has been initialized
from dbproject import routes
