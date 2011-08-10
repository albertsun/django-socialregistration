from django import template

register = template.Library()

@register.inclusion_tag('socialregistration/openid_form.html', takes_context=True)
def openid_form(context):
    if not 'request' in context:
        raise AttributeError, 'Please add the ``django.core.context_processors.request`` context processors to your settings.TEMPLATE_CONTEXT_PROCESSORS set'
    logged_in = context['request'].user.is_authenticated()
    if 'next_page' in context:
        next_page = context['next_page']
    else:
        next_page = None
    return dict(next=next_page, logged_in=logged_in, request=context['request'])
