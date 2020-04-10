def domain_name(url):
    if url.startswith('https://'):
        url = url[8:]
    if url.startswith('http://'):
        url = url[7:]
    if url.startswith('www.'):
        url = url[4:]
    s = ''
    for x in url:
        if x == '.':
            break
        s += x
    return s
