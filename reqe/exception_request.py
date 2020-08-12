import logging
import time

from functools import wraps

from reqe.utils import set_reqe_headers


def request_retry(exception):
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            retries = kwargs.pop("retries", 3)
            delay = kwargs.pop("delay", 1)
            backoff = kwargs.pop("backoff", 1)
            t = False
            while retries >= 0:
                try:
                    response = f(headers=set_reqe_headers(), *args, **kwargs)
                    t = True
                except exception as e:
                    if retries >= 1:
                        logging.warning(f"retrying {retries} times in {delay} seconds, {e}")
                        time.sleep(delay)
                    retries -= 1
                    delay *= backoff
                else:
                    return response
            if not t:
                return None

        return f_retry

    return deco_retry
