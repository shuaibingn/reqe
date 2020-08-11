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
