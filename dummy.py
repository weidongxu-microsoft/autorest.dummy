import sys
import json

length = -1
session_id = ''

while True:
    line = sys.stdin.readline()

    if line.find('Content-Length') >= 0:
        length = int(line.split(':', 2)[1])

    elif line.strip() == '':
        jsonstr = sys.stdin.read(length)

        jsondict = json.loads(jsonstr)
        method = jsondict['method']
        request_id = jsondict['id']

        if method == 'GetPluginNames':
            responsestr = json.dumps({
                'jsonrpc': '2.0',
                'id': request_id,
                'result': [
                    'dummy'
                ]
            })
            sys.stdout.write('Content-Length: {size}\n\n'.format(size=len(responsestr)))
            sys.stdout.write(responsestr)
            sys.stdout.flush()
        elif method == 'Process':
            session_id = jsondict['params'][1]
            responsestr = json.dumps({
                'jsonrpc': '2.0',
                'id': request_id,
                'result': True
            })
            sys.stdout.write('Content-Length: {size}\n\n'.format(size=len(responsestr)))
            sys.stdout.write(responsestr)
            sys.stdout.flush()
        elif method == 'Shutdown':
            break
        else:
            break
