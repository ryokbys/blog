#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ryo KOBAYASHI'
SITENAME = u'R.K.S. blog'
SITETITLE = u'R.K.S. blog'
SITESUBTITLE = u'Live as if you were to die tomorrow. Learn as if you were to live forever.'
SITETAG = 'R.K.S. blog'
#SITEURL = 'http://ryokbys.web.nitech.ac.jp/contents/blog'
SITEURL = 'http://ryokbys.github.io/blog/'
#SITEURL = 'file:///Users/kobayashi/Dropbox/Public/pelican_blog/output'
SITELOGO = SITEURL+'/images/yoda-and-me.png'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (
#     ('R.K.S. wiki', 'http://ryokbys.web.nitech.ac.jp/'),
# )

# # Social widget
# SOCIAL = (
#     ('Twitter', 'https://twitter.com/ryokbys',
#      'fa fa-twitter-square fa-fw fa-lg'),
#     ('LinkedIn', 'https://www.linkedin.com/home?trk=nav_responsive_tab_home',
#      'fa fa-linkedin-square fa-fw fa-lg'),
#     ('GitHub', 'http://github.com/ryokbys',
#      'fa fa-github-square fa-fw fa-lg'),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Extra stylesheets, for bootstrap overrides or additional styling.
#STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Whether or not to show authors in the article header
AUTHORS_IN_ARTICLE_HEADER = False
CATEGORIES_IN_ARTICLE_HEADER = False
TAGS_IN_ARTICLE_HEADER = True

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

SIDEBAR_HIDE_CATEGORIES = True

MARKUP = ['md', 'ipynb']
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud","render_math",'extract_toc','ipynb.markup']

#MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']
#MARKDOWN = ['codehilite','extra','smarty', 'toc']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# tag_cloud setting?
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
#THEME= './themes/my-theme-160103'
#THEME= '/Users/kobayashi/pelican-themes/Flex'
THEME= './themes/Flex'

#...Flex theme setting
# MAIN_MENU = True
# MENUITEMS = (('Archives', '/archives.html'),
#              ('Tags', '/tags.html'),)
# BROWSER_COLOR = '#888'
LINKS = (('Archives', SITEURL+'/archives.html'),
         ('Tags', SITEURL+'/tags.html'),)

# Added 2016.06.19
STATIC_PATHS = ['images', 'extra']
# EXTRA_PATH_METADATA = {
#     'images/yoda-and-me.png': {'path': 'yoda-and-me.png'},
# }

#PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
# DISPLAY_TAGS_ON_SIDEBAR_LIMIT = True
# DISPLAY_LINKS_ON_SIDEBAR_LIMIT = True
# LICENSE = 'MIT'
