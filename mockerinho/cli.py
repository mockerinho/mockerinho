import argparse
import os


def get_default_simulations_directory_path() -> str:
    directory = 'simulations/'
    cwd = os.path.abspath(os.getcwd())
    path = os.path.join(cwd, directory)
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='webapisimulator',
        description='Simulate Web APIs for development and testing purposes.',
    )

    parser.add_argument('-H', '--host',
                        help='specify server`s host', type=str, default='0.0.0.0')
    parser.add_argument('-p', '--port',
                        help='specify server`s port', type=int, default=8000)
    parser.add_argument('-D', '--directory',
                        help='specify simulations directory',
                        type=str,
                        default=get_default_simulations_directory_path())

    return parser.parse_args()


STARTING_SERVER_MESSAGE = '''
Starting Web API Simulator server at http://{}:{}
Quit the server with CONTROL-C.'''

SERVER_HAS_STOPPED_MESSAGE = 'Web API Simulator server has stopped.'


def main() -> None:
    args = parse_args()
    host, port, directory = args.host, args.port, args.directory

    try:
        print(STARTING_SERVER_MESSAGE.format(host, port))
        # server call goes here...
    except KeyboardInterrupt:
        print(SERVER_HAS_STOPPED_MESSAGE)
