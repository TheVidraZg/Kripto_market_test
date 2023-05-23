from flask import Flask , render_template


web_app = Flask(__name__)

#@web_app.route('http://192.168.1.201:5000/')
@web_app.route('/')
def index():
    #return f'<h1>Dobrodosli u Flask<h1><br/><p>Ovo je paragraf<p>'
    return render_template('index.html')

@web_app.route('/user/<name>')
def user_name(name):
    #return f'<h1>{str(name).upper()}, dobrodosli u FLASK<h1>'
    return render_template('user_name.html', name_varijabla =str(name).capitalize())
    
if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)
    