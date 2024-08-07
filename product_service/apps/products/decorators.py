from functools import wraps
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication


def auth_required(func):
    @wraps(func)
    def wrapped_view(*args, **kwargs):
        request = args[1]
        authenticator = TokenAuthentication()
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'token':
            raise AuthenticationFailed(
                'Authentication credentials were not provided.',
            )

        try:
            user_auth_tuple = authenticator.authenticate(request)

            if user_auth_tuple is not None:
                request.user, request.auth = user_auth_tuple
                return func(*args, **kwargs)

        except AuthenticationFailed as e:
            raise AuthenticationFailed('Invalid token.')

        raise AuthenticationFailed(
            'Authentication credentials were not provided.',
        )

    return wrapped_view
