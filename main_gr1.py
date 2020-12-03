from bottle import route, run, template, error, view, static_file

@route('/')
def index():
  return 'Append "tax/&lt;state,amount&gt;" to the URL to calculate the total after tax.' \
     '</br>Example:    tax/NY,250'

@route('/tax/<param>')
@view('core_gr1')
def index(param):
  return dict(param=param)


@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
  return static_file(filename, root='images')


run(host='localhost', port=8000, debug=True, reloader=True)