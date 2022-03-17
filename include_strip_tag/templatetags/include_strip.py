from django.template.loader_tags import do_include, IncludeNode
from django.template.library import Library
register = Library()

class StripIncludeNode(IncludeNode):
    def render(self, context):
        return super(StripIncludeNode, self).render(context).strip()

@register.tag("include_strip")
def do_include_strip(parser, token):
    result = do_include(parser, token)
    if isinstance(result, IncludeNode):
        result.__class__ = StripIncludeNode
    return result
