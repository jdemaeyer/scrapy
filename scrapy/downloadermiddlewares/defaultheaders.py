"""
DefaultHeaders downloader middleware

See documentation in docs/topics/downloader-middleware.rst
"""

from scrapy.utils.conf import remove_none_values


class DefaultHeadersMiddleware(object):

    def __init__(self, headers):
        self._headers = headers

    @classmethod
    def from_crawler(cls, crawler):
        headers = remove_none_values(crawler.settings['DEFAULT_REQUEST_HEADERS'])
        return cls(headers.items())

    def process_request(self, request, spider):
        for k, v in self._headers:
            request.headers.setdefault(k, v)
