import os, multiprocessing
from ack_api import app





if __name__ == "__main__":
    port = int(os.environ.get("PORT", "2890"))
    #pool = multiprocessing.Pool()
    app.run( host="0.0.0.0",port=port, debug=True)
