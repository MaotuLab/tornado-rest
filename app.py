from flask import Flask,abort
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mtapi'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/rest'

mongo = PyMongo(app)


@app.route('/')
def index():
    return 'Hello World!'



@app.route('/users', methods=['GET'])
def users_query():
  Users = mongo.db.users
  models = Users.find()
  output = []
  print(models)
  for item in models:
    output.append({'name' : item['name'], 'pwd' : item['pwd']})
  return jsonify({'result' : output})


@app.route('/users', methods=['POST'])
def users_add():
  Users = mongo.db.users
  user =request.json

  _id = Users.insert(user)

  result = Users.find_one({'_id': _id })
  print(result)
  return jsonify({'result' : 'ok'})

# @app.route('/modify/<string:name>', methods=['PUT'])
# def update_user(name):
#     user = mongo.db.userInfo.find({"name":name})
#     output = []
#     for s in user:
#       output.append({'name': s['name'], 'pwd': s['pwd']})
#     if len(output) == 0:
#       abort(404)
#     mongo.db.userInfo.update({"name":name},{'$set':{"name":"LZ111"}})
#     return jsonify({'result': output})
#
# @app.route('/delete/<string:name>', methods=['DELETE'])
# def delete_user(name):
#     user = mongo.db.userInfo.find({"name": name})
#     output = []
#     for s in user:
#       output.append({'name': s['name'], 'pwd': s['pwd']})
#     if len(output) == 0:
#       abort(404)
#     mongo.db.userInfo.remove({'name': name})
#     return jsonify({'result': True})
#


if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port = 80, debug = True)
    app.run()