

from flask import Flask,request,jsonify
import jwt, datetime
app=Flask(__name__)
SECRET='abnj'
@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    if data['username']=='Sreeja' and data['password']=='23456':
        token=jwt.encode(
            {'user':'Sreeja','exp':datetime.datetime.utcnow()+datetime.timedelta(hours=1)},
            SECRET,
            algorithm='HS256'
        )
        return jsonify(token=token)
    return jsonify(msg='Invalid'),401

@app.route('/protected')
def protected():
    token=request.headers.get('Authorization','').replace('Bearer','')

if __name__=="__main__":
    app.run(debug=True)