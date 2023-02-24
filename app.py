from flask import Flask, render_template

#here app is just an object of the class Flask
#by below we created a flask application
app = Flask(__name__) # in python __name__ is used for how a particular script was invoked, like if the script is invoked by python app.py then it has '__main__' as o/p & if u use other the ans will be different
@app.route('/')
def hello_world():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)