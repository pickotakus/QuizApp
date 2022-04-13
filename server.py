from flask import Flask
from flask import request
from flask import render_template, make_response

app = Flask(__name__)

def loadAllPictures():
  filepath = 'picDB.txt'
  pictures=[]
  with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
      if line!='':
        fullPicInfo = line.strip().split(';')
        pictures.append(fullPicInfo[1])
      line = fp.readline()
      cnt += 1
  fp.close()
  return pictures

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
  if not request.args.get('language'):
    return render_template("indexLV.html")
  else:
    return render_template("indexEN.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
    parametri = ["IQ","Augums","Māja"]
    images = loadAllPictures()
    return render_template("test.html",parametri=parametri,images=images)

#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "Viss kārtībā!"

if __name__ == '__main__':
  app.run(debug="true")
