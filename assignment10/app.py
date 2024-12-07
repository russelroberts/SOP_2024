from flask import Flask, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

#Load Database configuration settings

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'trialdb_sa'
app.config['MYSQL_PORT'] = 13306 #3306 port already in use by mariadb
app.config['MYSQL_PASSWORD'] = 'assignment10'
app.config['MYSQL_DB'] = 'trial_db'
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

#testing connection to db
@app.route('/fetch-data')
def fetch_data(): # would enclose in try catch here in production?
    cursor = mysql.connection.cursor()
    cursor.execute("SHOW TABLES;")  # Example query to list tables in the database
    tables = cursor.fetchall()
    cursor.close()
    return f"Tables in database: {tables}"


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Retrieve form data
        fullname = request.form.get('fullname')
        dob = request.form.get('dob')
        sex = request.form.get('sex')
        genderidentity = request.form.get('genderidentity')
        sexualorientation = request.form.get('sexualorientation')
        
       
            # Insert data into the database
        cursor = mysql.connection.cursor()
        query = """
            INSERT INTO personal_profile (fullname, dob, sex, genderidentity, sexualorientation)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (fullname, dob, sex, genderidentity, sexualorientation))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('profile'))
    elif request.method == 'GET':    # Render form template for GET requests 
      return render_template('profile.html')

if __name__ == "__main__":
    app.run(debug=True)
