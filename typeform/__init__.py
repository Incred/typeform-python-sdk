from .forms import Forms
from .themes import Themes
from .images import Images
from .responses import Responses
from .client import Client

__all__ = ['Typeform']


class Typeform:
    """Typeform API client"""

    def __init__(self, token: str, headers: dict = None):
        """Constructor for Typeform API client"""
        if headers is None:
            headers = {}
        client = Client(token, headers=headers)
        self._forms = Forms(client)
        self._themes = Themes(client)
        self._images = Images(client)
        self._responses = Responses(client)

    @property
    def forms(self) -> Forms:
        return self._forms

    @property
    def themes(self) -> Themes:
        return self._themes

    @property
    def images(self) -> Images:
        return self._images

    @property
    def responses(self) -> Responses:
        return self._responses
