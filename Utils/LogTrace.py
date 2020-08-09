from Models import Traces
from db import add_object


def log_trace(api_name, trace_id, status, message, request_json, response_json):
    """Log the APIs call to the database

    :param api_name: The APIs name
    :param trace_id: The trace Id
    :param status: The status of the call, ie. 200,404, etc.
    :param message: The message sent to the client
    :param request_json: The request from the client
    :param response_json: The response to the client
    """
    trace = Traces(api_name=api_name, trace_id=trace_id, status=status, message=message, request_json=request_json,
                   response_json=response_json)
    add_object(trace)
