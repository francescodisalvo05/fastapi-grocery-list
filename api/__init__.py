from flask import Flask 

app = Flask('Test API')
app.debug = True

with app.app_context():
    import api.greetings