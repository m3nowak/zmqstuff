'''
Simple zmq client
'''
import time

import zmq

CONTEXT = zmq.Context.instance()


def main():
    '''
    Runzmq client
    '''
    sock = CONTEXT.socket(zmq.PUSH)
    sock.connect('tcp://127.0.0.1:6094')
    for i in range(100):
        time.sleep(3)
        cool_msg = "xD x {}".format(i)
        print("Sending {}".format(cool_msg))
        sock.send_string(cool_msg)

if __name__ == "__main__":
    main()
