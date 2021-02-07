import sys, os
from flask import Flask , json, jsonify, render_template, abort, url_for
import json

app = Flask(__name__, template_folder='.')



# read file
with open('books.json', 'r') as myfile:
    data = myfile.read()




#Une home page à la racine de votre application (/) avec un titre "hello my app"
@app.route("/")
def index():
    return "hello my app "

#faite une route `/api/books` avec une méthode `GET` qui retourne cette variable sous forme de json 
@app.route("/api/books", methods=['GET'])
def books():
    # book=[
    #     {
    #         'id':1,
    #         'titre' : 'un titre',
    #     },
    #     {
    #         'id':2,
    #         'titre': 'un autre titre random',
    #     }
    # ]
    # return jsonify(book)
    return render_template('/Statics/index.html', title="page", jsonfile=json.dumps(data))


#faite une route qui retourne un book selon son `id`     
@app.route("/api/books/<int:id>", methods=['GET'])
def getbook(id):
    book=[
        {
            'id':1,
            'titre' : 'un titre',
        },
        {
            'id':2,
            'titre': 'un autre titre random',
        }
    ]
    return jsonify(book[id])

#faite une route qui retourne un book selon son titre 
# @app.route("/api/books/<titre>", methods=['GET'])
# def getbooktitle(titre):
#     book=[
#         {
#             'id':1,
#             'titre' : 'un titre',
#         },
#         {
#             'id':2,
#             'titre': 'un autre titre random',
#         }
#     ]
#     for i in range(len(book)):
#         if titre == book[i].titre : 
#             return jsonify(book[i])

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)
