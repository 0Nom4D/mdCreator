#!/usr/bin/env python3

from urllib.parse import urlencode, quote_plus
from typing import Union
import requests
import json


class ApiError(Exception):
    """
    Exception raised when error occurs in ApiLoader.

    Attributes
    ----------
    message : str
        Exception explanation
    """

    def __init__(self, message="Error while searching Gifs from API!"):
        """
        Constructs an actual Api Error Exception class.

        Parameters
        ----------
        message : str
            Message explaining the ApiError
        """
        self.message = message

    def __str__(self):
        """
        Returns the actual error message.

        Returns
        -------
        Actual Api Error message.
        """
        return f'ApiError: {self.message}'


class ApiLoader:
    """
    Class making every Tenor Api handling.

    Class is basically developed to be a "generic Tenor's Api wrapper"

    Attributes
    -------
    _base_url : str
        Api base endpoint url
    _transformed_url : str
        Transformed url with parameters
    _limit : int
        Number of gif mdCreator is going to get from Tenor's Api
    _params : int
        Parameters to encode for the Api Request
    _build : int
        Boolean verifying if searching url is built
    """

    def __init__(self, url: str, limit: int = 5) -> None:
        """
        Constructs a new ApiLoader object.

        Parameters
        -------
        url : str
            Api base endpoint url
        limit : int
            Number of gif mdCreator is going to get from Tenor's Api
        """

        self._base_url = url
        self._transformed_url = ""
        self._limit = limit
        self._params = dict()
        self._build = False

    # Gifs Tenor API
    def build_url(self, search: str, api_key: str) -> None:
        """
        Create the url with baseUrl and encoded parameters.

        Returns
        -------
        None
        """
        if search in [None, '']:
            return

        url_link = self._base_url
        self._params = {
            "q": str(search),
            "key": api_key,
            "limit": str(self._limit),
            "media_filter": "minimal"
        }

        url_link += urlencode(self._params, quote_via=quote_plus)
        self._transformed_url = url_link
        self._build = True

    def set_limit(self, limit: int) -> None:
        self._limit = limit

    def is_url_build(self) -> bool:
        """
        Checks if Api Search Url is built.

        Returns
        -------
        Boolean describing the actual search url state

        True if search url is built

        False otherwise
        """
        return self._build

    def get_gifs(self) -> Union[None, list]:
        """
        Search for gifs depending on the actual searching arguments.

        It executes the search request and checks for the request return code.

        Returns
        -------
        Either None or a list of gifs urls
        """

        gifs_urls = []

        if self._build:
            r = requests.get(self._transformed_url)
            if r.status_code == 200:
                values = json.loads(r.content)
                for gif in values["results"]:
                    for media in gif["media"]:
                        gifs_urls.append(media["gif"]["url"])
            else:
                print(ApiError())
                return None
            return gifs_urls
        print(ApiError("ApiLoader Url isn't build!"))
        return None
