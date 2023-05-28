from flask import Flask, jsonify, render_template

from services.user_api import get_users_from_api, get_user_from_api


web_app = Flask(__name__)

@web_app.route('/')
def index():
    return render_template('index.html')


@web_app.route('/user')
def user_name():
    users = get_users_from_api()
    return render_template('users.html',
                           users = users)

@web_app.route('/users/<id>')
def get_user(id):
    user = get_user_from_api(int(id))
    return render_template('user.html',
                           user = user)


@web_app.route('/api/user')
def user_api():
    return ''


@web_app.route('/about-us')
def about_us():
    return render_template('about_us.html')




if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)