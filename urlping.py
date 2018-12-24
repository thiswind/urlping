#/usr/bin/env python

import requests
import datetime
import time

import argparse

def do_ping(url):
    start = datetime.datetime.now()
    r = requests.get(url)
    end = datetime.datetime.now()
    elapsed = end - start

    print('get response from:', url, '; status:', r.status_code, '; time elapsed(in seconds):', elapsed.total_seconds())

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
