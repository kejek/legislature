from django import template

register = template.Library()


@register.simple_tag
def bootstrap_css():
    tags = [
        '<link rel="stylesheet"'
        'href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">',
        '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js">'
        '</script>'
    ]
    return ''.join(tags)


@register.inclusion_tag('checkout/statusModal.html')
def status_modal():
    return{}


@register.inclusion_tag('checkout/fullscreenModal.html')
def fullscreen_modal():
    return{}