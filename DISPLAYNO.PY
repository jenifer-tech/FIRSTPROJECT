from flask import*
app=Flask(__name__)  

@app.route('/no/<int:no1>')
def n_int(no1):
    return "The given no is %d " %no1
    
@app.route('/no/<float:no1>')    
def n_floatt(no1):
    return "The given no is %f " %no1

@app.route('/no/<float:no1>')    
def n_float(no1):
    return "The given no is %f " %no1 

@app.route('/no/<name>')    
def s_string(name):
    return "The given text is {} ".format(name)       

if __name__=='__main__':
    app.run(debug=True)    