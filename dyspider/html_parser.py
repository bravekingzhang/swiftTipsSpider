# -*- coding: utf-8 -*-
import urlparse
from bs4 import BeautifulSoup
import re


class HtmlParser:
    def __init__(self):
        pass

    def _get_new_links(self, url, soup):
        links_to_be_return = set()
        # links = soup.findAll("a", href=re.compile(r"/html/gndy/[a-z]+/\d+/\d+.html"))
        # for link in links:
        #   links_to_be_return.add(urlparse.urljoin(url, link["href"]))
        return links_to_be_return

    def _get_new_content(self, url, soup):
        content_to_be_return = list()
        try:
            lis = soup.find_all("li", class_="post-stub post")
            for li in lis:
                content = {}
                content['tipsTitle'] = li.find("a", class_="js-ajax-link").find("h4", class_="post-stub-title").text
                content['tipsTitle'] += " | " + li.find("a", class_="js-ajax-link").find("time", class_="post-stub-date").text
                content['tipsUrl'] = urlparse.urljoin(url, li.find("a", class_="js-ajax-link")["href"])
                content_to_be_return.append(content)
        except:
            print "not content to be output"
            return None

        return content_to_be_return

    def parser_html_content(self, url, html_content):
        if html_content is None:
            return None, None
        soup_ojb = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")
        links = self._get_new_links(url, soup_ojb)
        content = self._get_new_content(url, soup_ojb)
        return links, content
