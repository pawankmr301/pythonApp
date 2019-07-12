from cgi import parse_qs, escape
import subprocess

def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    if environ['REQUEST_URI'] == "/appAddUser":
        name = d.get('name', [''])[0]
        name = escape(name)

        address = d.get('address', [''])[0]
        address = escape(address)

        phoneNo = d.get('phoneNo', [''])[0]
        phoneNo = escape(phoneNo)

        cmd = 'python addUser.py ' + name + ' "' + address + '" ' + phoneNo

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()

        status = '200 OK'
        response = "<h1 style='color:blue'>" + out + "</h1>"

        start_response(status, [('Content-Type', 'text/html')])
        return [response]

    elif environ['REQUEST_URI'] == "/appGetUser":
        name = d.get('name', [''])[0]
        name = escape(name)

        cmd = 'python getUser.py ' + name

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()

        status = '200 OK'
        start_response(status, [('Content-Type', 'text/html')])
        return [out]
