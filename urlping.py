#/usr/bin/env python3
import eventlet
eventlet.monkey_patch()


import requests
import datetime
import time
import argparse
from urllib.parse import urlparse
import validators


def do_ping(url):
    start = datetime.datetime.now()
    try:
        with eventlet.Timeout(10):  # timeout is 10 seconds
            r = requests.get(url, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        return 'RequestException: {}'.format(e)
    except eventlet.Timeout as e:
        return 'TIME OUT: {}'.format(e)
    end = datetime.datetime.now()
    elapsed = end - start

    if 'content-type' in r.headers.keys():
        content_type = r.headers['content-type']
    else:
        content_type = 'Unknown'

    if 'server' in r.headers.keys():
        server = r.headers['server']
    else:
        server = 'Unknown'

    line = '[{}] URL: {} CONTENT_TYPE: {} SERVER: {} STATUS: {} TIME(ms): {}'.format(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        r.url,
        content_type,
        server,
        r.status_code, 
        int(elapsed.total_seconds() * 1000)
    )

    return line

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('url', type=str, metavar='url to ping', help='url to ping')
    parser.add_argument('-t', '--times', type=int, required=False, help='total ping times. if not set it goes infinity.')
    # parser.add_argument('-g', '--log', type=str, required=False, help='log file path, . for current path')

    args = parser.parse_args()

    times = 3600 * 24 * 30 * 365 * 100 if not args.times else args.times
    url = args.url
    # log_path = args.log

    if not validators.url(url):
        print('ERROR: invalid URL. Please tell me a valid url such as http://www.ynu.edu.cn')
        return

    while True:
        line = do_ping(url)

        print(line)

        # if log_path:
            # url = urlparse(url)
            # log_file_name = url.hostname
            # with open('{}.log'.format(log_file_name), 'a') as f:
                # f.write('{}\n'.format(line))

        times -= 1
        if times <= 0:
            break
        
        time.sleep(1)
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print()
