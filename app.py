from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

#here app is just an object of the class Flask
#by below we created a flask application
app = Flask(
  __name__
)  # in python __name__ is used for how a particular script was invoked, like if the script is invoked by python app.py then it has '__main__' as o/p & if u use other the ans will be different


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
