# Import
from flask import Flask, render_template,request, redirect
import flask_sqlalchemy



app = Flask(__name__)

#Feedback
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DBNAME.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = flask_sqlalchemy.SQLAlchemy(app)
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    def __repr__(self):
            return f'<Feedback {self.id}>'

# Esecuzione della pagina dei contenuti
@app.route('/', methods=["POST","GET"])
def index():
    if request.method == 'POST':
        email_var=request.form['email']
        text_var=request.form['text']
        feedback_var = Feedback(email= email_var, text= text_var)
        db.session.add(feedback_var)
        db.session.commit()
        return render_template('index.html')
    else:
         return render_template("index.html")

@app.route('/photoshop')
def photoshop():
    return render_template('photoshop.html')

@app.route('/editingvideo')
def capcut():
    return render_template('capcut.html')


@app.route('/database_plot')
def database_plot():
    # Visualizzazione delle voci del database
    feedbacks = Feedback.query.order_by(Feedback.email).all()
    return render_template('plot.html', feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)

