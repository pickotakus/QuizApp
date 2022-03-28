from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
    parametri = ["IQ","Augums","Kājas izmērs"]
    images = ["https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=49ed3252c0b2ffb49cf8b508892e452d","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/best-boy-cat-names-1606242656.jpg","https://www.rd.com/wp-content/uploads/2021/01/GettyImages-1175550351.jpg"]
    return render_template("test.html",parametri=parametri,images=images)

#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "Viss kārtībā!"

if __name__ == '__main__':
  app.run(debug="true")
