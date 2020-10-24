from flask import session
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        if user:
            return f(*args, **kwargs)
        return 'You need to login to view this page'
    return decorated_function


def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = dict(session).get('profile', None)
            if user and user["access_level"] >= access_level:
                return f(*args, **kwargs)
            return 'You need higher permissions to view this'
        return decorated_function
    return decorator