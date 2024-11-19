AUTHOR = 'Angel_Luis-Nauzet-Angel_Perez'
SITENAME = 'Canary'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

THEME = 'themes/hide'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Angel Luis', 'https://github.com/Angel-L-G'),
    ('Nauzet', 'https://getpelican.com/'),
    ('Angel Perez', 'https://github.com/NauzetPM'),
    ('Python.org', 'https://www.python.org/'),
    ('Pelican', 'https://getpelican.com/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

# Social widget
SOCIAL = (('Youtube', 'https://www.youtube.com/@ibb007'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MENU_LINKS = [
    ('Principal', 'welcome-to-canary.html'),
    ('Productos y Servicios', 'productos-y-servicios.html'),
    ('Reseñas', 'testimonios-de-clientes.html'),
    ('Contact', 'contacto.html'),
]

MENUITEMS = [
    ('Productos y Servicios', 'productos-y-servicios.html'),
    ('Reseñas', 'testimonios-de-clientes.html'),
    ('Contact', 'contacto.html'),
]
