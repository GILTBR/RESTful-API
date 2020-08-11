import sys

# from werkzeug.exceptions import HTTPException, BadRequest, NotFound
# from Utils.errors import NotFound
from flask_restx import Resource, fields, Namespace

from Models import Customers as Customers_model
from db import *
from . import api

ns = Namespace('Customers', description='Customers Model')
post_customer = api.model('Customers',
                          {'name': fields.String(description="Customer's name", required=True),
                           'email': fields.String(description="Customer's email", required=True)})


class CustomersApi(Resource):
    @staticmethod
    @api.doc(responses={400: 'Bad Request', 201: 'Customer created Successfully', 500: 'Internal Server Error'})
    @api.expect(post_customer, validate=True)
    def post():
        """Create a new customer in the database"""
        req = api.payload
        try:
            customer_name = req['name']
            customer_email = req['email']
            customer = Customers_model(name=customer_name, email=customer_email)
            add_object(customer)
            return {'message': f'Customer {customer_name} ({customer_email}) created!'}, 201
        except Exception as e:
            return 'Error on line {}: '.format(sys.exc_info()[-1].tb_lineno) + str(e), 500

    @staticmethod
    @api.doc(responses={400: 'Bad Request', 200: 'Success', 500: 'Internal Server Error'})
    def get():
        """Get a list of all customers"""
        try:
            customers = list_customers()
            response = [{'Name': customer.name, 'Email': customer.email, 'Created At': str(customer.created_at)} for
                        customer
                        in
                        customers]
            return {'Customers': response}, 200
        except Exception as e:
            return f'Error on line {format(sys.exc_info()[-1].tb_lineno)}: {str(e)}', 500


class CustomerApi(Resource):
    @staticmethod
    # @api.errorhandler(NotFound)
    @api.doc(responses={400: 'Bad Request', 404: 'Customer Not Found', 500: 'Internal Server Error'})
    def get(c_id):
        """Get info on a specific customer, based on his id"""
        try:
            customer = get_customer(Customers_model, c_id)
            if customer:
                response = {'Id': customer.id, 'Name': customer.name, 'Email': customer.email,
                            'Created At': str(customer.created_at)}
                return response, 200
            else:
                return 404
        except Exception as e:
            return f'Error on line {format(sys.exc_info()[-1].tb_lineno)}: {str(e)}', 500

    @staticmethod
    def delete(c_id):
        delete_object(Customers, c_id)
