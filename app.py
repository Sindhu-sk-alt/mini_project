from flask import Flask, render_template

flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    dic = {"name": "sindhu", "mobile": 7019816169}
    return render_template('index.html', context=dic)


@flask_app.route('/about-us')
def about_us():
    dic = {"college":"K S school og engineering and management"}
    return render_template('about.html',context=dic)


@flask_app.route('/contact-us')
def contact_us():
    dic = {"department":"computer science"}
    return render_template('contact.html',context=dic)


if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )
