# Error when submitting a password reset this is the error 
## TypeError

```
TypeError: unsupported operand type(s) for +: 'int' and 'bytes'
```

**Traceback (most recent call last):**

```
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 1498, in __call__
     return self.wsgi_app(environ, start_response)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 1476, in wsgi_app
     response = self.handle_exception(e)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 1473, in wsgi_app
     response = self.full_dispatch_request()
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 882, in full_dispatch_request
     rv = self.handle_user_exception(e)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 880, in full_dispatch_request
     rv = self.dispatch_request()
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 865, in dispatch_request
     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\flaskblog\routes.py", line 239, in reset_request
     send_reset_email(user)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\flaskblog\routes.py", line 223, in send_reset_email
     token = user.get_reset_token()
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\flaskblog\models.py", line 24, in get_reset_token
     return s.dumps({'user_id': self.id}).decode('utf-8')
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\serializer.py", line 317, in dumps
     rv = self.make_signer(salt).sign(payload)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\timed.py", line 51, in sign
     return value + sep + self.get_signature(value)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\signer.py", line 218, in get_signature
     key = self.derive_key()
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\signer.py", line 204, in derive_key
     bytes, self.digest_method(self.salt + b"signer" + secret_key).digest()
```

The above error occurred due to an unsupported operand type for the `+` operator between an `int` and `bytes`. To resolve this issue, you need to update your code to ensure that the operands are of compatible types.

You can use the `keycheck.py` script to check how your key is being encoded by `itsdangerous`. By running the command `python keycheck.py`, you can see the encoding result and configure the file accordingly with your key.
