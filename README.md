# Usage:

python3 urlping.py --url http://baidu.com --times 5

# Requirements

pip3 install -r requirements.txt

# Example

press `ctrl + c` to terminal 

```bash
$ python3 urlping.py --time 3600 --url http://baidu.com                                
[2018-12-24 14:26:58] url: http://baidu.com/ status_code: 200 elapsed_time: 150
[2018-12-24 14:26:59] url: http://baidu.com/ status_code: 200 elapsed_time: 80
[2018-12-24 14:27:00] url: http://baidu.com/ status_code: 200 elapsed_time: 77
[2018-12-24 14:27:01] url: http://baidu.com/ status_code: 200 elapsed_time: 77
[2018-12-24 14:27:02] url: http://baidu.com/ status_code: 200 elapsed_time: 78
[2018-12-24 14:27:03] url: http://baidu.com/ status_code: 200 elapsed_time: 79
[2018-12-24 14:27:04] url: http://baidu.com/ status_code: 200 elapsed_time: 77
[2018-12-24 14:27:05] url: http://baidu.com/ status_code: 200 elapsed_time: 76
[2018-12-24 14:27:06] url: http://baidu.com/ status_code: 200 elapsed_time: 78
[2018-12-24 14:27:08] url: http://baidu.com/ status_code: 200 elapsed_time: 77
[2018-12-24 14:27:09] url: http://baidu.com/ status_code: 200 elapsed_time: 78
[2018-12-24 14:27:10] url: http://baidu.com/ status_code: 200 elapsed_time: 301
[2018-12-24 14:27:11] url: http://baidu.com/ status_code: 200 elapsed_time: 78
[2018-12-24 14:27:12] url: http://baidu.com/ status_code: 200 elapsed_time: 82
[2018-12-24 14:27:13] url: http://baidu.com/ status_code: 200 elapsed_time: 78
[2018-12-24 14:27:14] url: http://baidu.com/ status_code: 200 elapsed_time: 81
```

OR in short way:

```bash
$ python3 urlping.py  -u http://baidu.com                                              
[2018-12-24 14:28:26] url: http://baidu.com/ status_code: 200 elapsed_time: 161
[2018-12-24 14:28:27] url: http://baidu.com/ status_code: 200 elapsed_time: 84
[2018-12-24 14:28:28] url: http://baidu.com/ status_code: 200 elapsed_time: 84
[2018-12-24 14:28:29] url: http://baidu.com/ status_code: 200 elapsed_time: 84
```