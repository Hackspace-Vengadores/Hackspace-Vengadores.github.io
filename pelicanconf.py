#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hackspace Vengadores'
SITENAME = 'Hackspace Vengadores'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Lima'

DEFAULT_LANG = 'en'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = 'themes/elegant'

MARKUP = ['md']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
		'markdown.extensions.toc': {}
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['./plugins', './plugins_community']
PLUGINS = [
	'neighbors',
	'latex-prerender',
	'liquid_tags.img',
	'liquid_tags.video',
	'liquid_tags.include_code',
	'liquid_tags.literal',
	'pelican-ipynb.liquid',
	'pelican-ipynb.markup',
	'summary',
	'extract_toc',
	'assets',
	'share_post',
	'series'
]

IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = './downloads/code'
NOTEBOOK_DIR = './downloads/notebooks'

IPYNB_USE_METACELL = True

STATIC_PATHS = ['downloads', 'images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
		 ('Python.org', 'http://python.org/'),
		 ('Jinja2', 'http://jinja.pocoo.org/'),
		 ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('RSS', 'https://hackspace-vengadores.github.io/feeds/all.atom.xml'),
		  ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

APPLAUSE_BUTTON = True
SOCIAL_PROFILE_LABEL = 'Mantente en contacto'
SHARE_POST_INTRO = 'Compárteme con tus amigos en'
SERIES_TITLE = 'Más en esta serie'

AUTHORS = {
    "BrendaCorrea111": {
        "url": "https://github.com/BrendaCorrea111",
        "blurb": "Ingeniera informática con pasión en la matemática.",
        "avatar": "https://avatars2.githubusercontent.com/u/59841016?s=400&v=4",
    },
    "Oromion": {
        "url": "https://github.com/carlosal1015",
        "blurb": "Estudiante de matemática con gusto en GNU/Linux.",
        "avatar": "https://avatars1.githubusercontent.com/u/21283014?s=460&v=4",
    },
    "AntonioAllende": {
        "url": "https://github.com/AntonioAllende",
        "blurb": "Estudiante de ingeniería de sistemas.",
		"avatar": "https://avatars2.githubusercontent.com/u/25266127?s=460&v=4",
    },
	"Darkil-HS": {
        "url": "https://github.com/Darkil-HS",
        "blurb": "Estudiante de ingeniería de sistemas.",
		"avatar": "https://avatars1.githubusercontent.com/u/59841028?s=460&v=4",
    },
	"MarlonX-HS": {
        "url": "https://github.com/MarlonX-HS",
        "blurb": "Estudiante de ingeniería de sistemas.",
		"avatar": "https://avatars0.githubusercontent.com/u/59841113?s=460&v=4",
    },
}