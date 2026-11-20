# flask is a web microframework

# se instalează cu
# pip install flask

# acest exemplu se rulează cu:
# flask --debug --app d5_ex6_simple_web_app_with_flask run 
# (comandă în shell-ul de sistem)


from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def home():
    return '<p>Salutare lume!!!</p>'


@app.route('/pagina-noua')
def newpage():
    return '<p>Ok, I\'m a new page</p>'


user_dict = {
    "john": {
        "name": "John One",
        "age": 40,
    },
    "joanne": {
        "name": "Joanne Two",
        "age": 22,
    },
    "dan": {
        "name": "Dan The Dan",
        "age": 52,
    },
    "anne": {
        "name": "Queen Anne",
        "age": 32,
    },
}


@app.route('/users')
def users():
    items = [
        f'<li><a href="/users/{id}">{user['name']}</a></li>'
        for id, user in user_dict.items()
    ]
    return f"""
        <ul>
            {"".join(items)}
        </ul>
    """


@app.route('/users/<id>')
def user(id):
    # aici ne-am duce în baza de date
    # și am lua obiectul user, și am randa pagina

    try:
        user = user_dict[id]
    except KeyError:
        # this user does not exist
        abort(404)

    return f'<p>Salutare. Tu ești: {user['name']} și ai {user['age']} ani!</p>'
