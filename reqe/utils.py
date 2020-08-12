from requests.utils import CaseInsensitiveDict


def set_reqe_user_agent(name='https://github.com/ophlr/reqe'):
    """
    Return a string representing the default user agent.

    :rtype: str
    """
    return '%s' % name


def set_reqe_headers():
    """
    :rtype: requests.structures.CaseInsensitiveDict
    """
    return CaseInsensitiveDict({
        'User-Agent': set_reqe_user_agent(),
        'Accept-Encoding': ', '.join(('gzip', 'deflate')),
        'Accept': '*/*',
        'Connection': 'keep-alive',
    })


# -------------------------------------------------------------------------


def validate_params(retries, delay, backoff):
    retries = validate_number_type(retries)
    delay = validate_number_type(delay)
    backoff = validate_number_type(backoff)
    if retries * delay * backoff < 0:
        raise Exception("reqe params must be positive")
    if isinstance(retries, float):
        raise Exception("retries must be int type")
    return retries, delay, backoff


def validate_number_type(number):
    if isinstance(number, int):
        return number
    elif isinstance(number, str):
        if number.isdigit():
            return int(number)
        elif number.count(".") == 1 and number.replace(".", "").isdigit():
            return float(number)
        else:
            raise Exception("error number type")
    elif isinstance(number, float):
        return number
    else:
        raise Exception("error number type")
