from urllib.parse import urlencode


def build_url_with_params(url: str, params: dict = None) -> str:
    if params is None:
        params = {}
    encoded = urlencode(clean_params(params))
    return url if (len(encoded) == 0) else (url + '?' + encoded)


def clean_params(params: dict = None) -> dict:
    if params is None:
        params = {}
    result = {}
    for key, value in params.items():
        if value is None:
            continue
        # Check If List
        if isinstance(value, list):
            result[key] = ','.join(map(str, value))
        # Check If Boolean
        elif isinstance(value, bool):
            result[key] = 'true' if value else 'false'
        # Everything Else (Strings/Numbers)
        else:
            result[key] = value
    return result
