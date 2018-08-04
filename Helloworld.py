from flask import Flask,render_template
import ldap

app = Flask(__name__)


@app.route('/')
def hello_world():
    ldap_server = "ldap://172.29.97.1:3268"
    username = "diagram"
    password = "mus!@#EWQ"
    # the following is the user_dn format provided by the ldap server
    user_dn = "uid=" + username + ",cn=mus_service,ou=adm_account,ou=nonorg,dc=eus,dc=mediatek,dc=inc"
    # adjust this to your base dn for searching
    base_dn = "dc=EUS,dc=mediatek,dc=inc"
    connect = ldap.initialize(ldap_server)
    search_filter = "uid=" + username
    try:
        # if authentication successful, get the full user data
        print("before1111")
        connect.bind_s(user_dn, password)
        print("before")
        result = connect.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
        print("after")
        # return all user data results
        connect.unbind_s()
        print(result)
    except ldap.LDAPError:
        connect.unbind_s()
        print("authentication error")
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
