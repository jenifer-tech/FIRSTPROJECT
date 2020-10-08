def square(n):
    a=n*n
    return a

def aplusb(n1,n2):
    b=square(n1)+2*n1*n2+square(n2)    
    return b


from flask import*
app=Flask(__name__)  

@app.route('/square/<int:n1>/<int:n2>')
def pyth(n1,n2):
    res=aplusb(n1,n2)
    return "A blus B  the whole square is {}".format(res)

 
if __name__=='__main__':
    app.run(debug=True) 
    