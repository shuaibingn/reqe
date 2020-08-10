# how to use reqe
from reqe import reqe

# use default setting, it can be used like request
response = reqe.get("https://www.baidu.com")
print(response.status_code)

# specify the params that you like
# retries: How many retries
# delay: time between two requests
# backoff: delay = delay * backoff
response = reqe.get("https://www.google.com", retries=3, delay=3, backoff=2, timeout=(2, 2))
print(response)
