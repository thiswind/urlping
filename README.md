# Usage:

python3 urlping.py --url http://baidu.com --times 5

# Requirements

pip3 install -r requirements.txt

# example

```bash
$ python3 urlping.py --times 5 --url http://baidu.com
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.148769
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.079198
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.074791
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.070363
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.073712

```

OR in short way:

```bash
$ python3 urlping.py -t 3 -u http://baidu.com
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.136462
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.071704
get response from: http://baidu.com ; status: 200 ; time elapsed(in seconds): 0.070892
```