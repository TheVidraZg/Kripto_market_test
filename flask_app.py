from flask import Flask, jsonify, render_template
import json


first_name_to_display = "Iva"
last_name_to_display = "Ivic"
email_to_display = "Iva.Ivic@domena.hr"

user_dict = {
        "name": f"{first_name_to_display} {last_name_to_display}",
        "email": email_to_display
    }



@web_app.route('/user')
def user_name():
    # Dohvatimo podatke iz baze - dodijelimo varijabla u templateu
    #return f'<h1>{str(name).upper()}, dobro dosli u Flask</h1>'
    return render_template('user_name.html',
                           email=email_to_display,
                           first_name=first_name_to_display,
                           last_name=last_name_to_display)


@web_app.route('/api/user')
def user_api():
    #return json.dumps(user_dict)
    return jsonify(user_dict)






if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000, debug=True)