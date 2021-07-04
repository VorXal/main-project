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
    for attr in data.keys():
        if attr == 'ip':
            geolocation_info.append(data[attr])
        elif attr == 'city':
            geolocation_info.append(data[attr])
        else:
            break
    return geolocation_info
