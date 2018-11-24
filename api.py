from flask import Flask, request
from flask_api import status
import multiprocessing, os, time
from ackermann import ack, tup_ack

pool = multiprocessing.Pool()
queue = multiprocessing.Queue()


app = Flask(__name__)


@app.route('/ack')
def do_ack():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    tup_list = [(m, n)]
    st_time = time.time()
    pool.map(tup_ack, tup_list)
    #p = multiprocessing.Process(target=ack, args=(arg_tup, queue)
    #p.start()
    end_time = time.time()
    print('Done it took {} Seconds'.format(end_time - st_time))
    return 'ok', status.HTTP_200_OK


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "2890"))
    app.run( host="0.0.0.0",port=port)