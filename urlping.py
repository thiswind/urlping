import requests
import datetime

import sys
import getopt

def main(argv):
    url = argv[0]

    # url = 'http://xk.ynu.edu.cn'

    start = datetime.datetime.now()
    r = requests.get(url)
    end = datetime.datetime.now()
    elapsed = end - start

    print('get response from', url, '; status:', r.status_code, '; time elapsed(in seconds):', elapsed.total_seconds())


if __name__ == '__main__':
    main(sys.argv[1:])
