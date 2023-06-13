from django import template

from Trip.models import Trip
from datetime import datetime
from re import findall

register = template.Library()
#
@register.simple_tag
def get_date():
    return datetime.now().strftime("%Y-%m-%d")


@register.simple_tag
def username_post_created(pk):
    return Trip.objects.get(pk=pk).trip_user.username

@register.simple_tag
def number_phone_post_created(pk):
    return Trip.objects.get(pk=pk).trip_user.number_phone

@register.simple_tag
def delete_account(pk):
    return Trip.objects.filter(pk=pk).delete()

import re
@register.simple_tag
def get_search_notes(url, categories):
    # query_where_from = str(re.findall(r".+where_from=([\w\%\-]+)&.+", str(url), re.ASCII)[-1])
    # query_where = str(re.findall(r".+where=([\w\%\-]+)&.+", str(url), re.ASCII)[0])
    # query_when = str(url).split("&")[-1].split("=")[-1]
    
    info = {
        "where_from" : str(re.findall(r".+where_from=([\w\%\-]+)&.+", str(url), re.ASCII)[-1]),
        "where" : str(re.findall(r".+where=([\w\%\-]+)&.+", str(url), re.ASCII)[0]),
        "when" : str(url).split("&")[-1].split("=")[-1],
    }

    return info[categories]

# @register.simple_tag
# def get_time_trip_url(url):
#     return 'time_trip?{0}'.format(url.split("?")[-1])

# @register.simple_tag
# def get_cost_url(url):
#     return 'cost?{0}'.format(url.split("?")[-1])

