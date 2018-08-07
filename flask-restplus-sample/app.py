from flask import Flask, Response
from flask_restplus import Api, Resource, fields
import psycopg2

app = Flask(__name__)

print (__name__)

api = Api(app, version='1.0', title='FlastRestPlus Tutorial API',
          description='A simple FlastRestPlus Tutorial API',
          )

ns = api.namespace('tutorial', description='Tutorial Flast Restplus')


customermodel = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'name': fields.String(required=True, description='The task details')
})

class CustomerDAO(object):

    def get(self):
        try:
            conn = psycopg2.connect("dbname='postgres' user='docker' host='localhost' password='docker'")
        except:
            print ("I am unable to connect to the database")
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)

DAO = CustomerDAO()

@ns.route('/customers')
class CustomerList(Resource):

    def get(self):
        DAO.get()
        return Response(response="{'message':'Success'}")
    @api.expect(customermodel)
    def post(self):
        return Response(response="{'message':'Success'}")


@ns.route('/customers/<custid>')
class Customer(Resource):

    def get(self):
        return Response(response="{'message':'Success'}")
    def put(self):
        return Response(response="{'message':'Success'}")

    def delete(self):
        return Response(response="{'message':'Success'}")




if __name__ == '__main__':
    app.run(debug=True)