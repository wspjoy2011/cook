from django import template

register = template.Library()


@register.filter
def textlist(iterable, count=None):
    result = ""
    index = 0

    for item in iterable.split('\n'):
        if '<p>' in item:
            if count is not None:
                index += 1
                result += f'<li><span><b>{index}</b>.</span> {item}</li><br>\n'
            else:
                result += f'<li>{item}</li>\n'

    return result


@register.filter
def counttime(text):
    return int(len(text.split()) / 100)
