# crud operation
from flask import Flask, jsonify, request

app=Flask(__name__)

Sreeja= [
    {"id":1, "title": "Sreeja"},
    {"id":2, "title": "Lingampally"},
    {"id":3, "title": "Pride and prejudiece"}
]

@app.route('/Sreeja', methods = ['GET','POST'])
def books_list():
    if request.method == 'GET':
        return jsonify(Sreeja)
    data = request.json
    new_books={"id":len(Sreeja)+1, "title":data['title']}
    Sreeja.append(new_books)
    return jsonify(new_books), 201

@app.route("/books/<int:book_id>",methods=['GET','PATCH','DELETE'])
def single_book(book_id):
    book=next((b for b in Sreeja if b['id'] == book_id),None)
    if not book:
        return jsonify({"error":"Book Not Found"}),404
    if request.method=='GET':
        return jsonify(book)
    elif request.method=='PATCH':
        book['title']=request.json['title']
        return jsonify(book)
    elif request.method=='DELETE':
        Sreeja.remove(book)
        return "",204

if __name__=="__main__":
    app.run(debug=True)


