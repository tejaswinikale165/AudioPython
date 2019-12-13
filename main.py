#from flask_ngrok import run_with_ngrok
from flask import Flask,render_template
app = Flask(__name__, template_folder="templates")
   #starts ngrok when the app is run
@app.route('/')
def index():
   return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost')