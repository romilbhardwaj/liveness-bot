""" Prints the timestamp to the specified path

Use this to check liveness of spot instances
"""

import time
import argparse

def parse_args():
    """ Parse arguments """
    parser = argparse.ArgumentParser(description='Prints the timestamp to the specified path')
    parser.add_argument('--path', type=str, default='/tmp/myfile.txt', help='Path to write timestamp to')
    parser.add_argument('--prefix', type=str, default='', help='String to prefix')
    parser.add_argument('--frequency', type=int, default=1, help='Frequency to write to file at')
    return parser.parse_args()

def main():
    args = parse_args()
    while True:
        with open(args.path, 'w') as f:
            write_str = args.prefix + ' ' + str(time.time())
            print("Writing to file: {}".format(write_str))
            f.write(write_str)
            f.write('\n')
        time.sleep(args.frequency)

if __name__ == '__main__':
    main()
