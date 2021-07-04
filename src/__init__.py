from flask import Flask, jsonify
from flask_restx import Resource, Api



app = Flask(__name__)

api = Api(app)


class Test(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'test!'
        }


api.add_resource(Ping, '/test')