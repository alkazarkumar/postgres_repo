  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_1:test@localhost/first_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"id : {self.id} name : {self.name} email : {self.email}"


@app.route("/insert")
def index():
    data = Data(name="Alcazar",email="alcazar@gmail.com")
    db.session.add(data)
    db.session.commit()
    return "Done"  

@app.route("/show")
def index2():
    data = Data.query.all()
    print(data)
    return "Done" 
 
WITH
   name_for_summary_data AS (
      SELECT Statement)
   SELECT columns
   FROM name_for_summary_data
   WHERE conditions <=> (
      SELECT column
      FROM name_for_summary_data)
   [ORDER BY columns]

 SELECT FROM table_name
WHERE column LIKE 'XXXX%'

or

SELECT FROM table_name
WHERE column LIKE '%XXXX%'

or

SELECT FROM table_name
WHERE column LIKE 'XXXX_'

or

SELECT FROM table_name
WHERE column LIKE '_XXXX'

or

SELECT FROM table_name
WHERE column LIKE '_XXXX_'

if __name__ == "__main__":
    app.run(debug=True)
