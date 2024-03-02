from distutils.log import debug 
from fileinput import filename 
from flask import *
from flask_cors import CORS
 
app = Flask(__name__)   
CORS(app)

@app.route('/')   
def main():  
   return 'mm'




@app.route('/upload' , methods = ['POST'])   
def gg():   
#   if request.method == 'POST':   
    print('cc')
    fz = request.files['file'] 
    fz.save(fz.filename) 
    
    print("bb",fz.filename)

    f=open(fz.filename,'r')
    # print(f.read())
    countline=0
    countword=0
    charcount=0

    for i in f:
        countline=countline+1
        linelen=len(i.split())
        wordlist=i.split()
        countword=countword+linelen
        for word in wordlist:
            wordlen=len(word)
            charcount=charcount+wordlen

        print()

    print("countline:-->",countline)
    print("countword:-->",countword)
    print("countchar:-->",charcount)
    return [countline,countword,charcount]










app.run(debug=True,port=3000)