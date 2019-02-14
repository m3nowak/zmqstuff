'''
Simple zmq server
'''
import zmq

CONTEXT = zmq.Context.instance()


def main():
    '''
    Runzmq server
    '''
    sock = CONTEXT.socket(zmq.PULL)
    sock.bind('tcp://127.0.0.1:6094')
    while True:
        message = sock.recv()
        print(message)

if __name__ == "__main__":
    main()
