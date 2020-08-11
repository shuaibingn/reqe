import logging
import time

from functools import wraps

from reqe.utils import set_reqe_headers


def request_retry(exception):
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            retries = kwargs.pop("retries", 3)
            delay = kwargs.pop("delay", 3)
            backoff = kwargs.pop("backoff", 2)
            t = False
            while retries > 0:
                try:
                    response = f(headers=set_reqe_headers(), *args, **kwargs)
                    t = True
                except exception as e:
                    logging.warning(f"{e}, retrying in {delay} seconds")
                    if retries > 1:
                        time.sleep(delay)
                    retries -= 1
                    delay *= backoff
                else:
                    return response
            if not t:
                return None

        return f_retry

    return deco_retry
