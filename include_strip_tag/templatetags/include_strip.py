from django.template.loader_tags import do_include, IncludeNode
from django import template
register = template.Library()

class StripIncludeNode(IncludeNode):
    def render(self, context):
        return super(StripIncludeNode, self).render(context).strip()

def do_include_strip(parser, token):
    result = do_include(parser, token)
    if isinstance(result, ConstantIncludeNode):
        result.__class__ = StripConstantIncludeNode
    elif isinstance(result, IncludeNode):
        result.__class__ = StripIncludeNode
    return result

register.tag('include_strip', do_include_strip)
