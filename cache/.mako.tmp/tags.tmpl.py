# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1438849642.852232
_enable_loop = True
_template_filename = '/Users/nicolasf/anaconda3/anaconda/lib/python3.4/site-packages/nikola/data/themes/base/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        range = context.get('range', UNDEFINED)
        title = context.get('title', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        len = context.get('len', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
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
        range = context.get('range', UNDEFINED)
        title = context.get('title', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        len = context.get('len', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        def content():
            return render_content(context)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagindex">\n    <header>\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </header>\n')
        if cat_items:
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Categories")))
                __M_writer('</h2>\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                for i in range(indent_change_before):
                    __M_writer('                <ul class="postlist">\n')
                __M_writer('            <li><a class="reference" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
                if indent_change_after <= 0:
                    __M_writer('                </li>\n')
                for i in range(-indent_change_after):
                    __M_writer('                </ul>\n')
                    if i + 1 < len(indent_levels):
                        __M_writer('                    </li>\n')
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('        <ul class="postlist">\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer('                <li><a class="reference listtitle" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "tags.tmpl", "source_encoding": "utf-8", "filename": "/Users/nicolasf/anaconda3/anaconda/lib/python3.4/site-packages/nikola/data/themes/base/templates/tags.tmpl", "line_map": {"66": 4, "67": 7, "68": 7, "69": 9, "70": 10, "71": 11, "72": 11, "73": 11, "74": 13, "75": 14, "76": 15, "77": 17, "78": 17, "79": 17, "80": 17, "81": 17, "82": 18, "83": 19, "84": 21, "85": 22, "86": 23, "87": 24, "88": 28, "89": 29, "26": 0, "91": 29, "92": 32, "90": 29, "94": 34, "95": 35, "96": 36, "97": 36, "98": 36, "99": 36, "100": 36, "101": 39, "102": 41, "41": 2, "108": 102, "46": 42, "93": 33, "52": 4}}
__M_END_METADATA
"""
