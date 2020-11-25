"""
Given an NGINX log:

64-249-27-114.client.dsl.net - - [11/Mar/2004:14:53:12 -0800] "GET /SpamAssassin.html HTTP/1.1" 200 7368
pd9eb1396.dip.t-dialin.net - - [11/Mar/2004:15:17:08 -0800] "GET /AmavisNew.html HTTP/1.1" 200 2300
10.0.0.153 - - [11/Mar/2004:15:51:49 -0800] "GET / HTTP/1.1" 304 -
10.0.0.153 - - [11/Mar/2004:15:52:07 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419
10.0.0.153 - - [11/Mar/2004:15:52:07 -0800] "GET /twiki/pub/TWiki/TWikiLogos/twikiRobot46x50.gif HTTP/1.1" 304 -
10.0.0.153 - - [11/Mar/2004:15:52:12 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419

Produce a list of the top hosts that returned return code NNN, and the count of that code.

Example output for code 200:

host,count
10.0.0.153,2
pd9eb1396.dip.t-dialin.net,1
64-249-27-114.client.dsl.net,1

Ref:
https://www.mkyong.com/nginx/count-ip-address-in-nginx-access-logs/
https://www.pythonforbeginners.com/code-snippets-source-code/python-script-monitor-apachenginx-log-file
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
https://askubuntu.com/questions/780601/how-to-monitor-syslog-and-get-alerted-when-there-is-a-certain-entry

https://docs.python.org/3/library/http.html
https://stackoverflow.com/questions/57156335/parsing-a-text-log-and-counting-occurrences-of-specific-events-errors

# ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
# ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"

"""

data = """
64-249-27-114.client.dsl.net - - [11/Mar/2004:14:53:12 -0800] "GET /SpamAssassin.html HTTP/1.1" 200 7368
pd9eb1396.dip.t-dialin.net - - [11/Mar/2004:15:17:08 -0800] "GET /AmavisNew.html HTTP/1.1" 200 2300
10.0.0.153 - - [11/Mar/2004:15:51:49 -0800] "GET / HTTP/1.1" 304 -
10.0.0.153 - - [11/Mar/2004:15:52:07 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419
10.0.0.153 - - [11/Mar/2004:15:52:07 -0800] "GET /twiki/pub/TWiki/TWikiLogos/twikiRobot46x50.gif HTTP/1.1" 304 -
10.0.0.153 - - [11/Mar/2004:15:52:12 -0800] "GET /twiki/bin/view/Main/WebHome HTTP/1.1" 200 10419
"""
import re
import operator

def get_statcode():
    return input("Please enter status code to count: ") or '200'

code_to_count = get_statcode()

data = [line.strip() for line in data.splitlines() if line.strip()]
counter_dict = {}
for line in data:
    hosts = re.match(r'^((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.){3}([A-Za-z0-9\-]+))', line)
    items = re.findall(r'(GET|POST).*?"\s(200|404|304)', line)
    stat_code = items[0][1]
    host = hosts.group()
    # print(items)

    if not hosts:
        continue
    if code_to_count != stat_code:
        continue

    counter_dict[host] = counter_dict.get(host,0) + 1

# for h, count in sorted(counter_dict.items(), key=operator.itemgetter(1), reverse=True):
print("The output of code {}: \n".format(code_to_count))
print("Host:  Count")
for h, count in sorted(counter_dict.items(), key=lambda item: item[1], reverse=True):
    print(h," :", count)
