# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'xim0608'
SITENAME = "til"
ALT_NAME = "#! " + SITENAME
SITESUBTITLE = "Random programming stuff"
DESCRIPTION = "xim0608's til"
SITEURL = 'https://til.ryuju.com'
FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'

META_IMAGE = SITEURL + "/static/img/og_logo.jpg"
META_IMAGE_TYPE = "image/jpeg"

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
LOCALE = 'ja_JP'

THEME = "themes/pelican-mg"

# Social widget
SOCIAL = (('github', 'https://github.com/xim0608'),)

SHARE = True

FOOTER = ("&copy; 2018 xim0608. All rights reserved.<br>" +
          "Code snippets in the pages are released under " +
          "<a href=\"http://opensource.org/licenses/MIT\" target=\"_blank\">" +
          "The MIT License</a>, unless otherwise specified.")


DEFAULT_PAGINATION = 10

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# TWITTER_USERNAME = 'luca_chr'
# DISQUS_SITENAME = "devsbytes"
# SC_PROJECT = '10224955'
# SC_SECURITY = '1f2cc438'