from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')
# this is how you define a function in Python
def index():
    # TODO: connect to DB

    # TODO: delete cucumber from basket_a
    # use function in util.py

    # TODO: check what is uniquely in basket_a but not in basket_b
    # use a varilable name record2 to store the sql results


    # TODO: disconnect from database


    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', log_html = record2)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

