
# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
CORS(app)
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()
        print(data)     # status code
        return {'data': "data"}
  
  
# another resource to calculate the square of a number

  
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')

  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)
