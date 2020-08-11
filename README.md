# reqe

A python network request library that will not throw exceptions

## Background

When timeout, network connection error, server error, etc., 
`requests` will raise the exception, there will be a lot of `try ... except ...` in the code.


Under the above problems, I developed a `reqe` based on the requests library, which is as simple as requests

## Usage

```python
import reqe

# use default settings, it can be used like request
response = reqe.get("https://www.baidu.com")
print(response)

# specify the params that you like
# retries: How many retries
# delay: time between two requests
# backoff: delay = delay * backoff
response = reqe.get("https://www.google.com", retries=3, delay=3, backoff=2, timeout=(2, 2))
print(response)


# how to use reqe with session
session = reqe.session()
response = session.get("https://www.baidu.com")
print(response)

response = session.get("https://www.google.com", retries=1, delay=3, backoff=2, timeout=(2, 2))
print(response)
```