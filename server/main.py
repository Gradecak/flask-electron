from flask_sqlalchemy import SQLAlchemy
from flask import Flask


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
  return app

app = create_app()
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return '<User %r>' % self.username
  def __str__(self):
    return 'id %s username %s email %s' % (self.id, self.username, self.email)

@app.route('/')
def hello_world():
  return User.query.all()[0].__str__()

if __name__ == "__main__":
  app.run(debug=True,
         host='0.0.0.0',
         port=9000,
         threaded=True)
