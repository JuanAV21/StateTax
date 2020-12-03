from bottle import route, run, template, error, view, static_file

@route('/')
@view('Home page.html')
def home():
    return dict()

@route('/tax/<param>')
@view('core_gr1')
def index(param):
  return dict(param=param)


@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
  return static_file(filename, root='images')

@error(500)
def error500(error):
    return '''
    <h1> Error 500: Must have been a bad input</h1>
    <button type="button" onclick="window.location='http://localhost:8000'">Click Me To Return!</button>
    '''

@error(404)
def error500(error):
    return '''
    <h1> Error 404: Sorry, but this page doesn't exist!</h1>
    <p> Try: http://localhost:8000/tax/(state abbreviation),(amount being spent)</p>
    <p> Be sure to remove the parentheses when doing your inputs, and don't forget the comma!</p>
    <button type="button" onclick="window.location='http://localhost:8000'">Click Me To Return!</button> '''
    

run(host='localhost', port=8000, debug=True, reloader=True)