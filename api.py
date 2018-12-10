from flask import Flask, request
from flask_api import status
import multiprocessing, os, time
from ackermann import ack, tup_ack, mt_ack, clack
from api import app
from utilities.tools import time_func

pool = multiprocessing.Pool()


@app.route('/ack')
def do_ack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    try:
        ans = time_func(ack, (m,n))
        print(str(ans))
        return str(ans), status.HTTP_200_OK
    except RecursionError as expected:
        return (str(expected) + '\n',
        status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

@app.route('/tupack')
def do_tupack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    to_pool = request.args.get('pool', "False")
    tup_list = [(m, n)]
    if to_pool == "True" or to_pool == "False":
        try:
            st_time = time.time()
            pool.map(tup_ack, tup_list)
            end_time = time.time()
            print('Done it took {} Seconds'.format(end_time - st_time))
            return 'ok', status.HTTP_200_OK
        except RecursionError as expected:
            return (str(expected) + '\n',
            status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
    else:
        try:
            st_time = time.time()
            tup_ack((m,n))
            end_time = time.time()
            print('Done it took {} Seconds'.format(end_time - st_time))
            return 'ok', status.HTTP_200_OK
        except RecursionError as expected:
            return (str(expected) + '\n',
            status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)


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

@app.route('/clack')
def do_clack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    try:
        st_time = time.time()
        c1 = clack()
        ans = c1.ack(m,n)
        end_time = time.time()
        print('Done it took {} Seconds'.format(end_time - st_time))
        print('Answer of ack({},{}) is {}'.format(m,n,ans))
        return ('Answer of ack({},{}) is {}'.format(m,n,ans) + '\n',
            status.HTTP_200_OK)
    except RecursionError as expected:
            return (str(expected) + '\n',
            status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "2890"))
    app.run( host="0.0.0.0",port=port)