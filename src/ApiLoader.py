#!/usr/bin/env python3

import requests
import json

class ApiError(BaseException):
    """Exception raised when error occurs in ApiLoader

    Attributes:
        message -- Message explanation
    """

    def __init__(self, message="Error while searching Gifs from API!"):
        self.message = message

    def __str__(self):
        return f'ApiError: {self.message}'

class ApiLoader:
    def __init__(self, url: str, search: str, limit: int = 5) -> None:
        self.baseUrl = url
        self.tranUrl = ""
        self.limit = limit
        self.search = search
        self.build = False

        self.buildUrl()

    #Gifs Tenor API
    def buildUrl(self):
        urlLink = self.baseUrl
        apikey = "CSGXSUKBREYZ"

        if self.search != "":
            urlLink += "q=" + str(self.search) + '&'
        urlLink += "key=" + apikey
        urlLink += "&limit=" + str(self.limit)
        urlLink += "&media_filter=minimal"
        self.tranUrl = urlLink
        self.build = True

    def searchGifs(self):
        gifsUrls = []

        if self.build:
            r = requests.get(self.tranUrl)
            if r.status_code == 200 or r.status_code == 202:
                values = json.loads(r.content)
                for gif in values["results"]:
                    for media in gif["media"]:
                        gifsUrls.append(media["gif"]["url"])
            else:
                print(ApiError())
                return (None)
            return (gifsUrls)
        print(ApiError("ApiLoader Url isn't build!"))
        return (None)