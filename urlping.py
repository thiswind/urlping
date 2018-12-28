#/usr/bin/env python

import requests
import datetime
import time
import argparse
from urllib.parse import urlparse
import eventlet

eventlet.monkey_patch()

def do_ping(url):
    start = datetime.datetime.now()
    try:
        with eventlet.Timeout(10):  # timeout is 10 seconds
            r = requests.get(url)
    except requests.exceptions.RequestException as e:
        print('RequestException: {}'.format(e))
        return
    except eventlet.Timeout as e:
        print('timeout: {}'.format(e))
        return
    end = datetime.datetime.now()
    elapsed = end - start

    line = '[{}] url: {} status_code: {} elapsed_time(ms): {}'.format(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        r.url,
        r.status_code, 
        int(elapsed.total_seconds() * 1000)
    )

    print(line)

    url = urlparse(url)
    
    log_file_name = url.hostname

    with open('{}.log'.format(log_file_name), 'a') as f:
        f.write('{}\n'.format(line))

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', required=True, help='url to ping')
    parser.add_argument('-t', '--times', type=int, required=False, help='total ping times. if not set it goes infinity.')

    args = parser.parse_args()

    times = 4 if not args.times else args.times
    url = args.url

    while True:
        do_ping(url)

        times -= 1
        if times <= 0:
            break
        
        time.sleep(1)
        

if __name__ == '__main__':
    main()
