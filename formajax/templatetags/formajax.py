# -*- coding: utf-8 -*-
from django import template
from django.conf import settings

"""
Bootstrap Base JS and CSS
"""
BOOTSTRAP_BASE_URL = getattr(settings, 'BOOTSTRAP_BASE_URL',
                             'http://twitter.github.io/bootstrap/assets/'
)

BOOTSTRAP_JS_BASE_URL = getattr(settings, 'BOOTSTRAP_JS_BASE_URL',
                                BOOTSTRAP_BASE_URL + 'js/'
)

BOOTSTRAP_JS_URL = getattr(settings, 'BOOTSTRAP_JS_URL',
                           None
)

BOOTSTRAP_CSS_BASE_URL = getattr(settings, 'BOOTSTRAP_CSS_BASE_URL',
                                 BOOTSTRAP_BASE_URL + 'css/'
)

BOOTSTRAP_CSS_URL = getattr(settings, 'BOOTSTRAP_CSS_URL',
                            BOOTSTRAP_CSS_BASE_URL + 'bootstrap.css'
)

"""
Form Malsup Base JS
"""
FORM_MALSUP_JS_BASE_URL = getattr(settings, 'FORM_MALSUP_JS_BASE_URL',
                                settings.STATIC_URL + 'js/'
)

FORM_MALSUP_JS_URL = getattr(settings, 'FORM_MALSUP_JS_URL',
                           None
)
"""
FORMAJAX Base CSS
"""
FORMAJAX_CSS_BASE_URL = getattr(settings, 'FORMAJAX_CSS_BASE_URL',
                                settings.STATIC_URL + 'css/'
)
FORMAJAX_CSS_URL = getattr(settings, 'FORMAJAX_CSS_URL',
                            FORMAJAX_CSS_BASE_URL + 'formajax.css'
)


register = template.Library()

@register.simple_tag
def bootstrap_stylesheet_url(css=None):
    """
    URL to Bootstrap Stylesheet (CSS)
    """
    url = BOOTSTRAP_CSS_URL
    if css:
        url = BOOTSTRAP_CSS_BASE_URL + u'bootstrap-%s.css' % css
    else:
        url = BOOTSTRAP_CSS_URL
    return url


@register.simple_tag
def bootstrap_stylesheet_tag(css=None):
    """
    HTML tag to insert Bootstrap stylesheet
    """
    return u'<link rel="stylesheet" href="%s">' % bootstrap_stylesheet_url(css)


@register.simple_tag
def bootstrap_javascript_url(name=None):
    """
    URL to Bootstrap javascript file
    """
    if BOOTSTRAP_JS_URL:
        return BOOTSTRAP_JS_URL
    if name:
        return BOOTSTRAP_JS_BASE_URL + 'bootstrap-' + name + '.js'
    else:
        return BOOTSTRAP_JS_BASE_URL + 'bootstrap.min.js'


@register.simple_tag
def bootstrap_javascript_tag(name=None):
    """
    HTML tag to insert bootstrap_toolkit javascript file
    """
    url = bootstrap_javascript_url(name)
    if url:
        return u'<script src="%s"></script>' % url
    return u''

@register.simple_tag
def formajax_stylesheet_url(css=None):
    """
    URL to Formajax Stylesheet (CSS)
    """
    url = FORMAJAX_CSS_URL
    if css:
        url = FORMAJAX_CSS_BASE_URL + u'formajax.%s.css' % css
    else:
        url = FORMAJAX_CSS_URL
    return url


@register.simple_tag
def formajax_stylesheet_tag(css=None):
    """
    HTML tag to insert Formajax stylesheet
    """
    return u'<link rel="stylesheet" href="%s">' % bootstrap_stylesheet_url(css)

@register.simple_tag
def form_malsup_javascript_url(name=None):
    """
    URL to Form Malsup javascript file
    """
    if FORM_MALSUP_JS_URL:
        return FORM_MALSUP_JS_URL
    if name:
        return FORM_MALSUP_JS_BASE_URL + 'jquery.form' + name + '.js'
    else:
        return FORM_MALSUP_JS_BASE_URL + 'jquery.form.min.js'


@register.simple_tag
def form_malsup_javascript_tag(name=None):
    """
    HTML tag to insert bootstrap_toolkit javascript file
    """
    url = form_malsup_javascript_url(name)
    if url:
        return u'<script src="%s"></script>' % url
    return u''