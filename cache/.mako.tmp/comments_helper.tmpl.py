# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438849642.589998
_enable_loop = True
_template_filename = '/Users/nicolasf/anaconda3/anaconda/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_link', 'comment_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        disqus = _mako_get_namespace(context, 'disqus')
        facebook = _mako_get_namespace(context, 'facebook')
        muut = _mako_get_namespace(context, 'muut')
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        comment_system = context.get('comment_system', UNDEFINED)
        isso = _mako_get_namespace(context, 'isso')
        livefyre = _mako_get_namespace(context, 'livefyre')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        disqus = _mako_get_namespace(context, 'disqus')
        facebook = _mako_get_namespace(context, 'facebook')
        muut = _mako_get_namespace(context, 'muut')
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        comment_system = context.get('comment_system', UNDEFINED)
        isso = _mako_get_namespace(context, 'isso')
        livefyre = _mako_get_namespace(context, 'livefyre')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link(link, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        disqus = _mako_get_namespace(context, 'disqus')
        facebook = _mako_get_namespace(context, 'facebook')
        muut = _mako_get_namespace(context, 'muut')
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        comment_system = context.get('comment_system', UNDEFINED)
        isso = _mako_get_namespace(context, 'isso')
        livefyre = _mako_get_namespace(context, 'livefyre')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_form(url, title, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper.tmpl", "source_encoding": "utf-8", "filename": "/Users/nicolasf/anaconda3/anaconda/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl", "line_map": {"22": 3, "25": 6, "28": 7, "31": 9, "34": 4, "37": 5, "40": 8, "43": 0, "48": 2, "49": 3, "50": 4, "51": 5, "52": 6, "53": 7, "54": 8, "55": 9, "56": 27, "57": 45, "58": 63, "64": 47, "76": 47, "77": 48, "78": 49, "79": 49, "80": 49, "81": 50, "82": 51, "83": 51, "84": 51, "85": 52, "86": 53, "87": 53, "88": 53, "89": 54, "90": 55, "91": 55, "92": 55, "93": 56, "94": 57, "95": 57, "96": 57, "97": 58, "98": 59, "99": 59, "100": 59, "101": 60, "102": 61, "103": 61, "104": 61, "110": 29, "122": 29, "123": 30, "124": 31, "125": 31, "126": 31, "127": 32, "128": 33, "129": 33, "130": 33, "131": 34, "132": 35, "133": 35, "134": 35, "135": 36, "136": 37, "137": 37, "138": 37, "139": 38, "140": 39, "141": 39, "142": 39, "143": 40, "144": 41, "145": 41, "146": 41, "147": 42, "148": 43, "149": 43, "150": 43, "156": 11, "168": 11, "169": 12, "170": 13, "171": 13, "172": 13, "173": 14, "174": 15, "175": 15, "176": 15, "177": 16, "178": 17, "179": 17, "180": 17, "181": 18, "182": 19, "183": 19, "184": 19, "185": 20, "186": 21, "187": 21, "188": 21, "189": 22, "190": 23, "191": 23, "192": 23, "193": 24, "194": 25, "195": 25, "196": 25, "202": 196}}
__M_END_METADATA
"""
