from flask import Flask,request
from flask_restful import Resource,Api
# 以上为引用，from是从哪里，import是导入，必须要from import

app = Flask(__name__)
api = Api(app)

todos = {}
# @app.route('/')
class HelloWorld(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(HelloWorld, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

