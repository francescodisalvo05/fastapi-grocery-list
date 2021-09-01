from flask import Flask 

if __name__ == '__main__':

    app = Flask('Test API')

    with app.app_context():
        import api.read
        import api.send