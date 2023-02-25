from flask import Flask, render_template, jsonify

#here app is just an object of the class Flask
#by below we created a flask application
app = Flask(__name__) # in python __name__ is used for how a particular script was invoked, like if the script is invoked by python app.py then it has '__main__' as o/p & if u use other the ans will be different

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id':3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    
  },
  {
    'id':4,
    'title': 'Backend Engineer',
    'location': 'Texas, USA',
    'salary': '$150,000'
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html', jobs = JOBS, company_name = 'Jovian')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)