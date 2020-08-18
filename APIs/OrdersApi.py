import sys

from flask_restx import Resource, fields, Namespace
from sqlalchemy.orm.exc import UnmappedInstanceError

from Models import Customers as Customers_model
from db import *
from . import api

ns = Namespace('Orders', description='Orders Model')


class OrdersApi(Resource):

    @staticmethod
    def get():
        """
        List all orders by a specific customer

        :return:
        """
        pass
