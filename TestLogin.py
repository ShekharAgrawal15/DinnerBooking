from flask import Flask
from flask.ext.ldap import LDAP, login_required

app = Flask(__name__)
app.debug = True

app.config['LDAP_HOST'] = 'ldap.example.com'
app.config['LDAP_DOMAIN'] = 'example.com'
app.config['LDAP_SEARCH_BASE'] = 'OU=Domain Users,DC=example,DC=com'

ldap = LDAP(app)
app.secret_key = "welfhwdlhwdlfhwelfhwlehfwlehfelwehflwefwlehflwefhlwefhlewjfhwelfjhweflhweflhwel"
app.add_url_rule('/login', 'login', ldap.login, methods=['GET', 'POST'])

@app.route('/')
@ldap.login_required
def index():
        pass

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     pass

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")