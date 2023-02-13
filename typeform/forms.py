import typing
from .client import Client


class Forms:
    """Typeform Forms API client"""
    def __init__(self, client: Client):
        """Constructor for Typeform Forms class"""
        self._client = client
        self._messages = FormMessages(client)

    @property
    def messages(self):
        return self._messages

    def create(self, data: dict = {}) -> dict:
        """Creates a form"""
        return self._client.request('post', '/forms', data=data)

    def delete(self, uid: str) -> str:
        """
        Deletes the form with the given form_id and all of the form's
        responses.
        Return a `str` based on success of deletion, `OK` on success,
        otherwise an error message.
        """
        return self._client.request('delete', f'/forms/{uid}')

    def get(self, uid: str) -> dict:
        """
        Retrieves a form by the given form_id. Includes any theme and
        images attached to the form as references.
        """
        return self._client.request('get', f'/forms/{uid}')

    def list(self, page: int = None, pageSize: int = None, search: str = None,
             workspace_id: str = None) -> dict:
        """
        Retrieves a list of JSON descriptions for all forms in your Typeform
        account (public and private).
        Forms are listed in reverse-chronological order based on the last date
        they were modified.
        """
        return self._client.request('get', '/forms', params={
            'page': page,
            'page_size': pageSize,
            'search': search,
            'workspace_id': workspace_id
        })

    def update(self, uid: str, data: dict = {},
               patch: bool = False) -> typing.Union[str, dict]:
        """
        Updates an existing form.
        Defaults to `put`.
        `put` will return the modified form as a `dict` object.
        `patch` will return a `str` based on success of change, `OK` on
        success, otherwise an error message.
        """
        method = 'patch' if patch else 'put'
        return self._client.request(method, f'/forms/{uid}', data=data)


class FormMessages:
    def __init__(self, client: Client):
        """Constructor for TypeForm FormMessages class"""
        self._client = client

    def get(self, uid: str) -> dict:
        """
        Retrieves the customizable messages for a form (specified by form_id)
        using the form's specified language.
        You can format messages with bold (*bold*) and italic (_italic_) text.
        HTML tags are forbidden.
        """
        return self._client.request('get', f'/forms/{uid}/messages')

    def update(self, uid: str, data: dict = None) -> str:
        if data is None:
            data = {}
        """
        Specifies new values for the customizable messages in a form
        (specified by form_id).
        You can format messages with bold (*bold*) and italic (_italic_) text.
        HTML tags are forbidden.
        Return a `str` based on success of change, `OK` on success, otherwise
        an error message.
        """
        return self._client.request('put', f'/forms/{uid}/messages',
                                    data=data)
