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
  if not request.cookies.get('language'):
    res = make_response('Set language')
    res.set_cookie('language', 'latvian')
    return render_template("indexLV.html")
  else:
    language = request.cookies.get('language')
    if language=='latvian':
      return render_template("indexEN.html")
    else:
      return render_template("aboutEN.html")

@app.route('/about')
def about():
  language = request.cookies.get('language')
  if language=='latvian':
    return render_template("aboutLV.html")
  else:
    return render_template("aboutEN.html")

@app.route('/test',methods = ['POST', 'GET'])
def test():
    parametri = ["IQ","Augums","Māja"]
    images = loadAllPictures()
    language = request.cookies.get('language')
    if language=='latvian':
      return render_template("testLV.html",parametri=parametri,images=images)
    else:
      return render_template("testEN.html",parametri=parametri,images=images)

#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "Viss kārtībā!"

if __name__ == '__main__':
  app.run(debug="true")
