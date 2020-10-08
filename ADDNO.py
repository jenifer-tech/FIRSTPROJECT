from flask import*
app=Flask(__name__)  

@app.route('/add/<int:no1>/<int:no2>')
def add_int(no1,no2):
    z=no1+no2
    return "The sum of the given  no is %d " %z
    
@app.route('/add/<float:no1>/<float:no2>')
def add_float(no1,no2):
    z=no1+no2
    return "The sum of the given floating no is {} ".format(z)


if __name__=='__main__':
    app.run(debug=True)    