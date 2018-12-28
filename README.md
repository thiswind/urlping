# Usage:

python3 urlping.py http://qq.com

# Requirements

pip3 install -r requirements.txt

# Example

press `ctrl + c` to terminal 

```bash
$ python3 urlping.py http://qq.com
[2018-12-28 23:11:55] URL: https://www.qq.com?fromdefault CONTENT_TYPE: text/html; charset=GB2312 SERVER: squid/3.5.24 STATUS: 200 TIME(ms): 1042
[2018-12-28 23:11:57] URL: https://www.qq.com?fromdefault CONTENT_TYPE: text/html; charset=GB2312 SERVER: squid/3.5.24 STATUS: 200 TIME(ms): 782
[2018-12-28 23:11:58] URL: https://www.qq.com?fromdefault CONTENT_TYPE: text/html; charset=GB2312 SERVER: squid/3.5.24 STATUS: 200 TIME(ms): 745
[2018-12-28 23:12:00] URL: https://www.qq.com?fromdefault CONTENT_TYPE: text/html; charset=GB2312 SERVER: squid/3.5.24 STATUS: 200 TIME(ms): 499
[2018-12-28 23:12:01] URL: https://www.qq.com?fromdefault CONTENT_TYPE: text/html; charset=GB2312 SERVER: squid/3.5.24 STATUS: 200 TIME(ms): 538
```

OR in short way:

```bash
$ python3 urlping.py http://qq.com -t 2
[2018-12-28 23:12:56] URL: https://www.qq.com?fromdefault CONTENT_TYPE: text/html; charset=GB2312 SERVER: squid/3.5.24 STATUS: 200 TIME(ms): 599
[2018-12-28 23:12:58] URL: https://www.qq.com?fromdefault CONTENT_TYPE: text/html; charset=GB2312 SERVER: squid/3.5.24 STATUS: 200 TIME(ms): 886
```

AND can be used in pipe:

```bash
$ for i in {1..4}; do python urlping.py http://qq.com -t 1 | awk '{print($13)}'; done;
540
506
543
519
```