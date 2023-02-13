import json
import requests
import typing

from .settings import API_BASE_URL
from .utils import build_url_with_params


class Client:
    """TypeForm API HTTP client"""

    def __init__(self, token: str, headers: dict = None):
        """Constructor for TypeForm API client"""
        if headers is None:
            headers = {}
        self._headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'bearer {token}'} | headers

    def request(self, method: str, url: str, data: dict = None,
                params: dict = {}, headers={}) -> typing.Union[str, dict]:
        if data is None:
            data = {}
        url = build_url_with_params((API_BASE_URL + url), params)
        headers = self._headers | headers
        response = requests.request(method, url, data=json.dumps(data),
                                    headers=headers)
        return self._validator(response)

    def _validator(self, response:
                   requests.Response) -> typing.Union[str, dict]:
        try:
            body = json.loads(response.text)
        except Exception:
            body = {}

        if isinstance(body, dict) and body.get('code', None):
            raise Exception(body.get('description'))
        elif response.status_code >= 400:
            msg = f'{response.status_code} {response.reason}'
            raise Exception(msg)
        elif len(response.text) == 0:
            return 'OK'
        else:
            return body
