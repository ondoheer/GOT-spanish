from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask.ext.stormpath import (
    StormpathManager,
    StormpathError,
    User,
    login_user,
    user,
    login_required,
    logout_user
)
from NPCgenerator import generateNPC
from housesGenerator import House
from holdings import Holdings


app = Flask(__name__, static_url_path='/static')
app.debug = True
stormpath_manager = StormpathManager(app)
app.config['SECRET_KEY'] = 'sdsd&#"dee!!!Deeeh8877'
app.config['STORMPATH_API_KEYFILE'] = '.keys/apiKey.properties'


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Allow users to register for the site."""
    if request.method == 'GET':
        return render_template('register.html')

    try:
        _user = stormpath_manager.application.accounts.create(
            {
                'email': request.form.get('email'),
                'password': request.form.get('password'),
                'username': request.form.get('user'),
                'given_name': request.form.get('first-name'),
                'surname': request.form.get('last-name'),


            }

        )
        _user.__class__ = User
    except StormpathError, err:
        return render_template('register.html', error=err.message)

    login_user(_user, remember=True)
    return redirect(url_for('.dashboard'))


# Map our custom login view to Flask-Stormpath.
stormpath_manager.login_view = '.login'


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Allow users to log into the site."""
    if request.method == 'GET':
        return render_template('login.html')

    try:
        _user = User.from_login(
            request.form.get('email'),
            request.form.get('password')
        )
    except StormpathError, err:
        return render_template('login.html', error=err.message)

    login_user(_user, remember=True)
    return redirect(request.args.get('next') or url_for('.dashboard'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Render a dashboard page for logged in users."""

    # Store some custom data in our user's account.
    user.custom_data['favorite_web_framework'] = 'Flask'
    user.save()

    return render_template('dashboard.html')

# Define la ruta inicial y la pagina a renderizar


@app.route('/logout')
def logout():
    """Log a user out of their account."""
    logout_user()
    return redirect(url_for('.index'))


@app.route('/')
def index():
    return render_template('index.html')

# Ruta fisica del generadorNPC


@app.route('/npc')
def npc():
    return render_template('npc.html')

# funcion de la aplicacion que corre el generador


@app.route('/NPCgenerator', methods=['GET'])
def NPCgenerator():
    generoRecibido = request.args['genero']
    if generoRecibido == 'hombre':
        genero = 'hombre'
    elif generoRecibido == 'mujer':
        genero = 'mujer'
    edad = request.args['edad']
    generatedNPC = generateNPC.generarNPC(genero, edad)
    return jsonify(generatedNPC)


# funcion que genera las casas
@app.route('/houses')
def houses():
    return render_template('houses.html')


@app.route('/houseGenerator', methods=['GET', 'POST'])
def houseGenerator():
    realm = request.args.get('realm')
    size = request.args.get('size')
    foundation = request.args.get('foundation')
    name = request.args.get('name')
    house = House.startingResources(realm, size, foundation, name)
    from holdings import holdingsData
    generatedHouse = Holdings(holdingsData).generateAllHoldings(house, realm)
    return jsonify(generatedHouse)


# funcion que calculara precios de items
@app.route('/store')
def store():
    return 'Pagina en construccion'


# funcion que calculara precios de items
@app.route('/character')
def other():
    return 'Aqui ira la hoja de personaje'

if __name__ == '__main__':
    app.run()
