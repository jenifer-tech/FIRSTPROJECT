from flask import*
app=Flask(__name__)  

@app.route('/sum/<int:n>')
def sum(n):
    sum=0
    for i in range (0,n+1):
        sum=sum+i
    return "The sum of the given no is {}".format(sum)

if __name__=='__main__':
    app.run(debug=True) 