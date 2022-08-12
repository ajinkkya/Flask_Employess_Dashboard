from urllib import response
from config import *


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!<h1>'

# Create - 'Crud'
# Endpoint for "Insert Record"
@app.route('/insert/', methods=['POST'])
def insert():
    emp_id = request.json['emp_id']
    emp_name = request.json['emp_name']
    emp_phone_no = request.json['emp_phone_no']
    emp_email = request.json['emp_email']
    cration_date = request.json['cration_date']
    is_active = request.json['is_active']
    

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=password,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                if emp_id and emp_name and emp_phone_no and emp_email and cration_date and is_active:
                    cur.execute('INSERT INTO employees(EMP_ID, EMP_NAME, emp_phone_no, EMP_EMAIL_ID, CREATION_DATE, IS_ACTIVE) VALUES (%s, %s, %s, %s, %s, %s)',
                                (emp_id, emp_name, emp_phone_no, emp_email, cration_date, is_active))
                    conn.commit()
                    success_output = {
                        "Massage" : f'For EMP ID - "{emp_id}", named - "{emp_name}". Record is submitted in Database successfully!',
                        "Response Code" : 200,
                        "Status" : "Success"
                    }
                    return make_response(jsonify(success_output), 200)
                    

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    failed_output = {
        "Massage" : f'For EMP ID - {emp_id}, named - {emp_name}. Record is failed to submit in Database!',
        "Reason" : f"{emp_id} is already assigned as Primary key in Emp ID Column in Databse, Try Diffrent Emp ID",
        "Response Code" : 500,
        "Status" : "Failed"
    }
    return make_response(jsonify(failed_output), 500)            
    

# Read - 'cRud'
# Endpoint for "Read Record"
@app.route('/read/', methods=['POST'])
def read():

    emp_id = request.json['emp_id']

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=password,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

                cur.execute(f"SELECT * FROM employees WHERE emp_id = {emp_id}")
                for record in cur.fetchall():
                    recordDict = {
                        "Emp_Id": record['emp_id'],
                        "Emp_Name": record['emp_name'],
                        "Emp_Phone_no": record['emp_phone_no'],
                        "Emp_Email_ED": record['emp_email_id'],
                        "Creation Date": record['creation_date'],
                        "Is_Active": record['is_active']
                    }
                return make_response(jsonify(recordDict), 200)

    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    failed_output = {
        "Massage" : f"For EMP ID - {emp_id}, Record is failed to read from Database!",
        "Response Code" : 500,
        "Reason" : f"{emp_id} is not availabe in Database EMP ID Column",
        "Status" : "Failed"
    }
    return make_response(jsonify(failed_output), 500)
    

# Update - 'crUd'
# Endpoint for "Update Record"
@app.route('/update/<int:emp_id>/<string:Emp_Phone_no>/<string:emp_email>', methods=['GET', 'POST'])
def update(emp_id, Emp_Phone_no, emp_email):
    
    try:
        with psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = password,
                    port = port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                
                if emp_id and Emp_Phone_no and emp_email:
                    update_script = f"UPDATE employees SET emp_phone_no = {Emp_Phone_no}, EMP_EMAIL_ID = {emp_email} WHERE emp_id = {emp_id}"
                    cur.execute(update_script)
                    
                    conn.commit()
                
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return f'''For EMP ID - "{emp_id}",\n
            Record is Updated in Database successfully!\n
            For Phone No - "{Emp_Phone_no},\n
            For Email Address "{emp_email}".'''
    
# Delete - 'cruD'
# Endpoint for "Delete Record"
@app.route('/delete/<int:emp_id>>', methods=['GET', 'POST'])
def delete(emp_id):
    
    try:
        with psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = password,
                    port = port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                
                if emp_id:
                    cur.execute(f'DELETE FROM employees WHERE emp_id = {emp_id}')
                    
                    conn.commit() 
                
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return f'For EMP ID - "{emp_id}", Record is Deleted from Database successfully!'

if __name__ == "__main__":
    app.run(debug=True)