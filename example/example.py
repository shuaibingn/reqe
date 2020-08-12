import reqe

# use reqe like requests
# retries = 3s
# delay = 1s
# backoof = 1
response = reqe.get("https://www.google.com")
if response:
    print(response.status_code)

# customize the parameters of reqe
response = reqe.get("https://www.gooogle.com", retries=2, delay=3, backoff=2, timeout=(2, 2))
if response:
    print(response.status_code)
print(response)
