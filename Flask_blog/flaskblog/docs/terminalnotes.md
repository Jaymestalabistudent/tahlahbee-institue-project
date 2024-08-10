notes

- Flask is a micro web framework written in Python
- Flask is lightweight and modular
- Flask is easy to learn and simple to use
- Flask is designed to make getting started quick and easy, with the ability to scale up to complex applications
- Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine
- Flask is BSD-licensed
- Flask is used by Pinterest and LinkedIn
- Flask is a good choice for building web applications

to run base app in python add this code to a file called flaskblog.py so it reloads automatically when updated in  development

```python
if __name__ == '__main__':
app.run(debug=True)
```

The line `if __name__ == '__main__':` is a common pattern in Python that checks if the current module is being run directly as the main program. In this case, it is used to ensure that the following code is only executed when the file is run directly.

The line `app.run(debug=True)` is used to start the Flask application. The `debug=True` parameter enables debug mode, which allows for automatic browser updates when changes are made to the code.

To run the application, you can open the terminal and enter `python flaskblog.py`. This will execute the file and start the Flask application in debug mode.
