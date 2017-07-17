from functools import wraps
from distutils.version import StrictVersion


def quiet_option(options, quiet_option_name='quiet'):
    def _impl(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if hasattr(options, quiet_option_name) and getattr(options, quiet_option_name):
                return None
            else:
                return func(*args, **kwargs)
        return wrapper
    return _impl