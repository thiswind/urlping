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

    parser.add_argument('--url', required=True, help='url to ping')
    parser.add_argument('--times', required=False, help='total ping times')

    args = parser.parse_args()

    times = int(args.times)
    url = args.url

    for i in range(times):
        do_ping(url)
        time.sleep(1)
        

if __name__ == '__main__':
    main()
