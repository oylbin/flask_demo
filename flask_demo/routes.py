from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from flask import current_app
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
from .services import loginservice

bp = Blueprint('flask_demo', __name__, template_folder="templates",
               static_folder='static')


@bp.route('/', methods=['GET'])
@login_required
def root_route():
    return render_template('index.html', name=current_user.id)


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if not loginservice.login(username, password):
            return redirect(url_for('.signin'))
        next_url = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        # if not is_safe_url(next):
        #    return flask.abort(400)
        return redirect(next_url or url_for('.root_route'))
    return render_template('signin.html')


@bp.route('/signout', methods=['GET'])
def signout():
    logout_user()
    return redirect(url_for('.root_route'))


@bp.route('/api/test', methods=['GET'])
@login_required
def api_test():
    return jsonify({'ret': 0,
                    'username': current_user.id,
                    'secret_key': current_app.config['SECRET_KEY']})
