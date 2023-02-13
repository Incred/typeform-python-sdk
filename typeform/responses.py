import typing
from .client import Client


class Responses:
    """Typeform Responses API client"""

    def __init__(self, client: Client):
        """Constructor for Typeform Responses class"""
        self._client = client

    def list(
        self, uid: str, pageSize: int = None, since: str = None,
        until: str = None, after: str = None, before: str = None,
        included_response_ids: str = None, completed: bool = None,
        sort: str = None, query: str = None, fields: typing.List[str] = None
    ) -> dict:
        """
        Returns form responses and date and time of form landing and submission.
        """
        return self._client.request('get', f'/forms/{uid}/responses', params={
            'page_size': pageSize or None,
            'since': since or None,
            'until': until,
            'after': after,
            'before': before,
            'included_response_ids': included_response_ids,
            'completed': completed,
            'sort': sort,
            'query': query,
            'fields': fields
        })

    def delete(self, uid: str, included_tokens:
               typing.Union[str, typing.List[str]]) -> str:
        """
        Delete responses to a form. You must specify the
        `included_tokens`/`includedTokens` parameter.
        Return a `str` based on success of deletion, `OK` on success,
        otherwise an error message.
        """
        return self._client.request(
            'delete',
            f'/forms/{uid}/responses',
            params={'included_tokens': included_tokens}
        )
