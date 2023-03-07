from django import template

register = template.Library()

@register.filter(name='sum_query_list')
def sum_query_list(queryarg):

    sum = 0
    for i in queryarg:
        sum += i.price

    return round(sum,2)

