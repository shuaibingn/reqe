# how to use reqe
import reqe

# use default setting, it can be used like request
response = reqe.get("https://www.baidu.com")
if response:
    print(response)

# specify the params that you like
# retries: How many retries
# delay: time between two requests
# backoff: delay = delay * backoff
response = reqe.get("https://www.google.com", retries=3, delay=3, backoff=2, timeout=(2, 2))
# when `requests` raise an exception, `reqe` will catch the exception and response is None
if response:
    print(response)


# how to use reqe with session
session = reqe.session()
response = session.get("https://www.baidu.com")
print(response)

response = session.get("https://www.google.com", retries=1, delay=3, backoff=2, timeout=(2, 2))
print(response)
