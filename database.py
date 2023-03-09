from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args={'ssl': {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs
  #print('Result Dict:', result_dicts)


#with engine.connect() as conn:
#  result = conn.execute(text("select * from jobs"))


def load_job_from_db(id):
  with engine.connect() as conn:
    query = text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id)
    result = conn.execute(query)
    row = result.fetchone()
    if not row:
      return None
    else:
      column_names = result.keys()
      return dict(zip(column_names, row))

  #print('type(result) :', type(result))
  #result_all = result.all()
  #print('type(result_all):', type(result_all))
  #first_result = result_all[0]
  #print('type(first_result) : ',type(first_result))
  #print('first_data', first_result)
  #first_result_dict = result_all[0]._mapping #this is working
  #print('type(first_result_dict)',type(first_result_dict))
  #print('fist_resut_dict:', first_result_dict)
  #function = load_jobs_from_db()
  #print('function:',function[0])
  #for cat in function:
  #  print(cat['title'])

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])