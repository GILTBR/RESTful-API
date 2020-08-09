import sys

from flask_restx import Resource, fields, Namespace

from Models import Customers
from . import api
from db import add_object, list_customers

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
        try:
            req = api.payload
        except Exception as e:
            return str(e), 400
        try:
            customer_name = req['name']
            customer_email = req['email']
            customer = Customers(name=customer_name, email=customer_email)
            add_object(customer)
            return {'name': customer_name, 'email': customer_email}, 201
        except Exception as e:
            return 'Error on line {}: '.format(sys.exc_info()[-1].tb_lineno) + str(e), 500

    @staticmethod
    @api.doc(responses={400: 'Bad Request', 200: 'Success', 500: 'Internal Server Error'})
    def get():
        """Get a list of all customers"""
        try:
            customers = list_customers()
            res = [{'Name': customer.name, 'Email': customer.email, 'Created At': str(customer.created_at)} for customer
                   in
                   customers]
            return {'Customers': res}, 200
        except Exception as e:
            return 'Error on line {}: '.format(sys.exc_info()[-1].tb_lineno) + str(e), 500
