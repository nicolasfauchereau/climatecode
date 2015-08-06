# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438849642.716062
_enable_loop = True
_template_filename = 'themes/zen/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('arusahni', context._clean_inheritance_tokens(), templateuri='arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'arusahni')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        helper = _mako_get_namespace(context, 'helper')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        helper = _mako_get_namespace(context, 'helper')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for post in posts:
            __M_writer('        <div class="post">\n            <h1 class="title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(str(post.title()))
            __M_writer('</a></h1>\n            <div class="meta">\n                <div class="authordate">\n                    <time class="timeago" datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('">')
            __M_writer(str(post.formatted_date(date_format)))
            __M_writer('</time>\n                </div>\n                <div class="stats">\n')
            if not post.meta('nocomments'):
                __M_writer('                    ')
                __M_writer(str(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer('\n')
            __M_writer('                </div>\n            ')
            __M_writer(str(arusahni.html_tags(post)))
            __M_writer('\n            </div>\n            <div class="body">\n')
            if index_teasers:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('            </div>\n        </div>\n')
        __M_writer('    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "source_encoding": "utf-8", "filename": "themes/zen/templates/index.tmpl", "line_map": {"22": 4, "25": 3, "28": 2, "34": 0, "49": 2, "50": 3, "51": 4, "52": 5, "57": 34, "63": 7, "77": 7, "78": 8, "79": 9, "80": 10, "81": 10, "82": 10, "83": 10, "84": 13, "85": 13, "86": 13, "87": 13, "88": 16, "89": 17, "90": 17, "91": 17, "92": 19, "93": 20, "94": 20, "95": 23, "96": 24, "97": 24, "98": 24, "99": 25, "100": 26, "101": 26, "102": 26, "103": 28, "104": 31, "105": 31, "106": 31, "107": 32, "108": 32, "109": 33, "110": 33, "116": 110}}
__M_END_METADATA
"""
