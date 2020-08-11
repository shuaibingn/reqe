# reqe

A python network request library that will not throw exceptions

## Table of Contents

- [Background](#Background)
- [Install](#Install)
- [Usage](#Usage)
- [Reference](#Reference)
- [License](#License)

## Background

When timeout, network connection error, server error, etc., 
`requests` will raise the exception, there will be a lot of `try ... except ...` in the code.


Under the above problems, I developed a `reqe` based on the requests library, which is as simple as requests

## Install

- #### source code

```shell script
git clone git@github.com:ophlr/reqe.git
```

- #### pip
```shell script
pip install reqe
```

## Usage

```python
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
# when `requests` raises an exception, `reqe` will catch it and let the response be None
if response:
    print(response)


# how to use reqe with session
session = reqe.session()
response = session.get("https://www.baidu.com")
print(response)

response = session.get("https://www.google.com", retries=1, delay=3, backoff=2, timeout=(2, 2))
print(response)
```

## Reference

[requests](#https://github.com/psf/requests)

## License
[Apache 2.0](./LICENSE)