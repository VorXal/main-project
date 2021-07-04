from json import load
from urllib.request import urlopen


def geolocation(addr=''):
    geolocation_info = []
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    data = load(res)
    geolocation_info.append(data['ip'])
    geolocation_info.append(data['city'])
    return geolocation_info
