import requests
import time
payload={'hdl':'10.1109/TFUZZ.2015.2426311'}
url="http://dx.doi.org/10.1109/TFUZZ.2015.2426311"
start = time.time()
TimeOut = 1
while True:
    try:
        r = requests.get(url, timeout = TimeOut)
        break
    except:
        TimeOut += 1

end = time.time()

print('TimeOut = {0}, Execution time = {1}, url = {2}'.format(TimeOut, end - start, r.url))