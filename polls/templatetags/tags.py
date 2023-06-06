from django import template

register = template.Library()


@register.filter(name='three_digits_show')
def three_digits_currency(value: int):
    return ' تومان' + ' ' + '{:,}'.format(value)


@register.simple_tag
def Sum(num1, num2):
    ans = num1 + num2
    return three_digits_currency(ans)
