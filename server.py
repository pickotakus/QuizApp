from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

@app.route('/test')
def test():
  parametri = ["Augums","Svars","Vecums"]
  return render_template("test.html",param=parametri)

@app.route('/about')
def about():
  return render_template("about.html")

if __name__ == '__main__':
  app.run(debug="true")
