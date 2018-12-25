#/usr/bin/env python

import requests
import datetime
import time
import argparse

def do_ping(url):
    start = datetime.datetime.now()
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        return "Error: {}".format(e)
    end = datetime.datetime.now()
    elapsed = end - start

    line = '[{}] url: {} status_code: {} elapsed_time(ms): {}'.format(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        r.url,
        r.status_code, 
        int(elapsed.total_seconds() * 1000)
    )

    print(line)

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
