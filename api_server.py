import argparse

from api import app


def run_api_server(args):

    app.run(host=args.host, port=args.port)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default='8080')

    arguments = parser.parse_args()

    run_api_server(arguments)