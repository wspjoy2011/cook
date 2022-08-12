from django import template

register = template.Library()


@register.filter
def textlist(iterable, count=None):
    result = ""
    for index, item in enumerate(iterable.split('\n')):
        print(f'<li>{index + 1} {item}</li><br>')
        if count is not None:
            result += f'<li><span><b>{index + 1}</b>.</span> {item}</li><br>\n'
        else:
            result += f'<li>{item}</li>\n'

    return result

