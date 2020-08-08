from Models import Traces
from run import Session, log


def log_trace(api_name, trace_id, status, message, request_json, response_jon):
    """Log the API call to the database

    :param api_name: The API name
    :param trace_id: The trace Id
    :param status: The status of the call, ie. 200,404, etc.
    :param message: The message sent to the client
    :param request_json: The request from the client
    :param response_jon: The response to the client
    """
    trace = Traces(APIName=api_name, TraceId=trace_id, Status=status, Message=message, RequestJSON=request_json,
                   ResponseJSON=response_jon)
    db_session = Session()

    try:
        db_session.add(trace)
        db_session.commit()
        log.debug('committed')
    except Exception as e:
        log.info(e)
        db_session.rollback()
        log.warning('rollback')
    finally:
        db_session.close()
        log.info('closed')
