import time
from flask import request
from flask_api import status
from ack_api import app
from ack_api.utilities.tools import time_func, return_func
from ack_api.custom_exceptions.exceptions import FunctionNotFound
from ack_api.ack_py.ackermann import Clack, MemoizedAck



@app.route('/ack-api-<string:tool>')
def do_ack(tool):
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    try:
        if tool == "memoized_ack":
            return "This tools is incompatible please go to /mlack", status.HTTP_409_CONFLICT
        func = return_func(tool)
        ans = time_func(func, (m,n))
        print(str(ans))
        return str(ans)
    except (RecursionError, FunctionNotFound) as expected:
        print(expected)
        return str(expected) + '\n'

@app.route('/cyack')
def do_cyack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    try:
        #ans = cy_ack.ack(m, n)
        # Will this even work
        ans = time_func(cy_ack, (m,n))
        print(str(ans))
        return str(ans), status.HTTP_200_OK
    except (RecursionError, FunctionNotFound) as expected:
        return (str(expected) + \
            '\ncy_ak might need to be compiled, check cy_ack folder\n')

@app.route('/clack')
def do_clack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    try:
        st_time = time.time()
        ans = Clack().ack(m,n)
        took = time.time() - st_time
        print('Done it took {} Seconds'.format(took))
        print('Answer of ack({},{}) is {}'.format(m,n,ans))
        to_answer = 'Answer of ack({},{}) is {}\nIt took: {}\n'.format(m,n,ans,took)
        return (to_answer,
            status.HTTP_200_OK)
    except RecursionError as expected:
            return (str(expected) + '\n')

@app.route('/mlack')
def do_mlack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    try:
        st_time = time.time()
        ans = MemoizedAck().ack(m,n)
        took = time.time() - st_time
        print('Done it took {} Seconds'.format(took))
        print('Answer of ack({},{}) is {}'.format(m,n,ans))
        to_answer = 'Answer of ack({},{}) is {}\nIt took: {}\n'.format(m,n,ans,took)
        return (to_answer,status.HTTP_200_OK)
    except RecursionError as expected:
            return (str(expected) + '\n')

# Unfinished
@app.route('/all')
def do_all():
    to_pass = []
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    tup_list = [(m, n)]
    try:
        st_time = time.time()
        ans = ack(m,n)
        end_time = time.time()
        print('Done it took {} Seconds'.format(end_time - st_time))
        print('Answer of ack({},{}) is {}'.format(m,n,ans))
        to_pass.append({"ack:", True})
    except RecursionError as expected:
        to_pass.append({"ack:", False})
    try:
        st_time = time.time()
        ans = tup_ack((m,n))
        end_time = time.time()
        print('Done it took {} Seconds'.format(end_time - st_time))
        print('Answer of ack({},{}) is {}'.format(m,n,ans))
        to_pass.append({"tupack:", True})
    except RecursionError as expected:
        to_pass.append({"tupack:", False})
    try:
        st_time = time.time()
        ans = tup_ack((m,n))
        end_time = time.time()
        print('Done it took {} Seconds'.format(end_time - st_time))
        print('Answer of ack({},{}) is {}'.format(m,n,ans))
        to_pass.append({"tupack:", True})
    except RecursionError as expected:
        to_pass.append({"tupack:", False})



""" Disabled
@app.route('/mtack')
def do_mtack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    if m + n >= 6:
        print("This crashes the sum of the 2 numbers can't be higher than 6")
        return ("This crashes the sum of the 2 numbers can't be higher than 6" + '\n',
        status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
    else:
        st_time = time.time()
        ans = mt_ack(m,n)
        end_time = time.time()
        print('Done it took {} Seconds'.format(end_time - st_time))
        print('Answer of ack({},{}) is {}'.format(m,n,ans))
        return ('Answer of ack({},{}) is {}'.format(m,n,ans) + '\n',
        status.HTTP_200_OK)
"""
