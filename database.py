from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,
                       connect_args = {
                         'ssl':{
                           "ssl_ca": "/etc/ssl/cert.pem"
                         }
                       }
                      )




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