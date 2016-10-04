import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
mysql = MySQL()
app = Flask(__name__, template_folder=tmpl_dir)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '0919'
app.config['MYSQL_DATABASE_DB'] = 'stock'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/add")
def add():
    return render_template('add.html')

@app.route('/search_stock',methods=['POST'])
def search_stock():
    temp = []
    info = []
    stockname = request.form['stockname']
    cursor = mysql.connect().cursor()
    cursor.execute("""SELECT * FROM new_table WHERE name = %s;""",(stockname,))
    rec=cursor.fetchall()
    if rec is None:
        context = "The stock is not in the database"
    else:
        #rec=cursor.fetchall()
        for row in rec:
            print(row)
            temp.append("StockPrice: "+str(row[0]))
            temp.append("StockName: "+str(row[1]))
        context = dict(info = temp)
    return render_template('search.html', **context)

@app.route('/add_stock',methods=['POST'])
def add_stock():
    name1 = request.form['stockname']
    price1 = request.form['stockprice']
    connection=mysql.get_db()
    cursor = connection.cursor()
    query="""INSERT INTO new_table (name,price) VALUES(%s,%s)"""
    cursor.execute(query,(name1,price1))
    connection.commit()
    return render_template('add_finish.html')

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
