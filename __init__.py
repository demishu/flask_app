from app import app, db
from urls import *
# import os


def main(host=None, port=None, debug=False):
    # if not os.path.exists('/templates'):
    #     os.makedirs('/templates')
    # if not os.path.exists('/database'):
    #     os.makedirs('/database')

    """default_values"""
    _host = '127.0.0.1'
    _port = '3000'
    _debug = True

    host = host or _host
    port = port or _port
    debug = debug or _debug
    with app.app_context():
        db.create_all()
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
