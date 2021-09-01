from flask import Flask 

app = Flask('Test API')

with app.app_context():
    import api.listen