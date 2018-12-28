#/usr/bin/env python3
import eventlet
eventlet.monkey_patch()


import requests
import datetime
import time
import argparse
from urllib.parse import urlparse


def do_ping(url):
    start = datetime.datetime.now()
    try:
        with eventlet.Timeout(10):  # timeout is 10 seconds
            r = requests.get(url, allow_redirects=True)
    except requests.exceptions.RequestException as e:
        return 'RequestException: {}'.format(e)
    except eventlet.Timeout as e:
        return 'timeout: {}'.format(e)
    end = datetime.datetime.now()
    elapsed = end - start

    line = '[{}] URL: {} CONTENT_TYPE: {} SERVER: {} STATUS: {} TIME(ms): {}'.format(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        r.url,
        r.headers['content-type'],
        r.headers['server'],
        r.status_code, 
        int(elapsed.total_seconds() * 1000)
    )

    return line

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', required=True, help='url to ping')
    parser.add_argument('-t', '--times', type=int, required=False, help='total ping times. if not set it goes infinity.')

    args = parser.parse_args()

    times = 4 if not args.times else args.times
    url = args.url

    while True:
        line = do_ping(url)

        print(line)

        # url = urlparse(url)
        # log_file_name = url.hostname
        # with open('{}.log'.format(log_file_name), 'a') as f:
            # f.write('{}\n'.format(line))

        times -= 1
        if times <= 0:
            break
        
        time.sleep(1)
        

if __name__ == '__main__':
    main()
