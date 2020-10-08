from flask import*
app=Flask(__name__)  

@app.route('/square/<int:n>')
def square(n):
    a=n*n
    return "Square of {} is {}".format(n,a)

@app.route('/square/<int:n1>/<int:n2>')
def aplusb(n1,n2):
    b=n1*n1+n2*n2+2*n1*n2

    return "{} plus {} the whole square is  {}".format(n1,n2,b)    

if __name__=='__main__':
    app.run(debug=True) 