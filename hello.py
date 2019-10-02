def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    print([bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
                  encoding="utf8")])
    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
                  encoding="utf8")]
