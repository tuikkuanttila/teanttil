import bottle

from bottle import Bottle, route, template


app = Bottle()

@app.route('/page/<page_name>')# Handle HTTP GET for the application root
def show_page(page_name):
    return template('page',page_name=page_name)

@app.route('/')
def index():
    return template('index_bootstrap')

@app.route('/about')
def about():
    return template('about')

# Run bottle internal test server when invoked directly ie: non-uxsgi mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
else:
    application = app

