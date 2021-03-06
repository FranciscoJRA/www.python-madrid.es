#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Python-Madrid'
SITENAME = u'Python-Madrid'
SITEURL = 'http://www.python-madrid.es'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'es'

# Blogroll
LINKS =  (
    ('Niwi.be', 'http://www.niwi.be/'),
    ('Pybonacci', 'http://pybonacci.wordpress.com/'),
    ('Python.org', 'http://python.org'),
)

SOCIAL = (
    ('twitter', "http://twitter.com/python_madrid"),
    ('github', "https://github.com/python-madrid"),
)

DEFAULT_PAGINATION = 5

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

ARTICLE_URL = 'post/{slug}/'
ARTICLE_SAVE_AS = 'post/{slug}/index.html'
STATIC_PATHS = ["pictures", ]
TEMPLATE_PAGES = {'pages/video-archives.html': 'video-archives.html'}

RELATIVE_URLS =  True
TWITTER_USERNAME = u"python_madrid"

GOOGLE_ANALYTICS = u"UA-29774405-1"
DISQUS_SITENAME = "pythonmadrid"
THEME = "themes/python-madrid"

DISPLAY_PAGES_ON_MENU = True
REVERSE_CATEGORY_ORDER = True

MENUITEMS = (
    ('videos', '/video-archives.html'),
)


STATIC_PATHS = [
    'extra/robots.txt',
    'files',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

LOCALE = "en"
