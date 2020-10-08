from flask import*
app=Flask(__name__)  

@app.route('/vote/<int:n>')
def vote(n):
    if n>=18:
        return "You are elligible for vote"
    else:    
        return "You are not elligible for vote"


if __name__=='__main__':
    app.run(debug=True) 