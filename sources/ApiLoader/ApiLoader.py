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
            Message explaning the ApiError
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
    _url : str
        Api base endpoint url
    _tranUrl : str
        Transformed url with parameters
    _limit : int
        Number of gif mdCreator is going to get from Tenor's Api
    _search : str
        Actual string build by every gif search keywords
    _params : int
        Parameters to encode for the Api Request
    _build : int
        Boolean verifying if searching url is built
    """

    def __init__(self, url: str, search: str, limit: int = 5) -> None:
        """
        Constructs a new ApiLoader object.

        Parameters
        -------
        _url : str
            Api base endpoint url
        _search : str
            Actual string build by every gif search keywords
        _limit : int
            Number of gif mdCreator is going to get from Tenor's Api
        """

        # Tenor API Key isn't protected or hidden because
        # I didn't find the best way to camouflage it
        self._apikey = "CSGXSUKBREYZ"
        self._baseUrl = url
        self._tranUrl = ""
        self._limit = limit
        self._search = search
        self._params = dict()
        self._build = False

        self.buildUrl()

    # Gifs Tenor API
    def buildUrl(self) -> None:
        """
        Create the url with baseUrl and encoded parameters.

        Returns
        -------
        None
        """
        urlLink = self._baseUrl
        self._params = {
            "q": str(self._search),
            "key": self._apikey,
            "limit": str(self._limit),
            "media_filter": "minimal"
        }

        urlLink += urlencode(self._params, quote_via=quote_plus)
        self._tranUrl = urlLink
        self._build = True

    def setLimit(self, limit: int) -> None:
        self._limit = limit

    def isUrlBuild(self) -> bool:
        """
        Checks if Api Search Url is built.

        Returns
        -------
        Boolean describing the actual search url state

        True if search url is built

        False otherwise
        """
        return self._build

    def searchGifs(self) -> Union[None, list]:
        """
        Search for gifs depending on the actual searching arguments.

        It executes the search request and checks for the request return code.

        Returns
        -------
        Either None or a list of gifs urls
        """

        gifsUrls = []

        if self._build:
            r = requests.get(self._tranUrl)
            if r.status_code == 200:
                values = json.loads(r.content)
                for gif in values["results"]:
                    for media in gif["media"]:
                        gifsUrls.append(media["gif"]["url"])
            else:
                print(ApiError())
                return None
            return gifsUrls
        print(ApiError("ApiLoader Url isn't build!"))
        return None
