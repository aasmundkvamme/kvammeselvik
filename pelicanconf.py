AUTHOR = 'Aasmund Kvamme'
SITENAME = 'KvammeSelvik'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
LOCALE = 'C.utf8'
# DEFAULT_LANG = 'en'

THEME = '../pelican-themes/gum'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#    ("Pelican", "https://getpelican.com/"),
#    ("Python.org", "https://www.python.org/"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Ulikt
LOAD_CONTENT_CACHE = False
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 25
SUMMARY_MAX_PARAGRAPHS = 4
PLUGINS = ['render_math',
    ]