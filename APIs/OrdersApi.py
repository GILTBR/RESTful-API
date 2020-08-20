import sys

from flask_restx import Resource, fields, Namespace
from sqlalchemy.orm.exc import UnmappedInstanceError

from Models import Customers as Customers_model
from db import *
from . import api

ns = Namespace('Orders', description='Orders Model')

items = api.model('items', {'item_id': fields.Integer(required=True), 'quantity': fields.Integer(required=True),
                            'price': fields.Float(required=True)})
# {"item_id": fields.Integer(required=True),
#          "quantity": fields.Integer(required=True),
#          'price': fields.Float(required=True)}

new_order = api.model('New Order',
                      {'customer_id': fields.Integer(required=True), 'items': fields.List(fields.Nested(items))})


class OrdersApi(Resource):

    @staticmethod
    def get():
        """
        List all orders by a specific customer

        :return:
        """
        pass

    @staticmethod
    @api.expect(new_order, validate=True)
    def post():
        """
        Create a new order

        :return:
        """

    pass


class OrderApi(Resource):

    @staticmethod
    def get(o_id):
        """
        View a specific order

        :return:
        """
        pass

    @staticmethod
    def post(o_id):
        """
        delete an order

        :return:
        """

    pass
