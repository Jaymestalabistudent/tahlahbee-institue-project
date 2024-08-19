I have been receiving this error when submitting a password reset this is the error 

TypeError
TypeError: unsupported operand type(s) for +: 'int' and 'bytes'

Traceback (most recent call last)
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 1498, in __call__
return self.wsgi_app(environ, start_response)
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 1476, in wsgi_app
response = self.handle_exception(e)
           ^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 1473, in wsgi_app
response = self.full_dispatch_request()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 882, in full_dispatch_request
rv = self.handle_user_exception(e)
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 880, in full_dispatch_request
rv = self.dispatch_request()
     ^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\flask\app.py", line 865, in dispatch_request
return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\flaskblog\routes.py", line 239, in reset_request
send_reset_email(user)
^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\flaskblog\routes.py", line 223, in send_reset_email
token = user.get_reset_token()
        ^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\flaskblog\models.py", line 24, in get_reset_token
return s.dumps({'user_id': self.id}).decode('utf-8') # return the token
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\serializer.py", line 317, in dumps
rv = self.make_signer(salt).sign(payload)
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\timed.py", line 51, in sign
return value + sep + self.get_signature(value)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\signer.py", line 218, in get_signature
key = self.derive_key()
      ^^^^^^^^^^^^^^^^^
File "F:\Github-Dev\tahlahbee-institute-project\Flask_blog\venv\Lib\site-packages\itsdangerous\signer.py", line 204, in derive_key
bytes, self.digest_method(self.salt + b"signer" + secret_key).digest()
                          ^^^^^^^^^^^^^^^^^^^^^
TypeError: unsupported operand type(s) for +: 'int' and 'bytes'
The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error.
To switch between the interactive traceback and the plaintext one, you can click on the "Traceback" headline. From the text traceback you can also create a paste of it. For code execution mouse-over the frame you want to debug and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some extra helpers available for introspection:

dump() shows all variables in the frame
dump(obj) dumps all that's known about the object


I used keycheck.py to see how my key was being translated by itsdangerous 

and the result was it was translating to bytes 
tis was due to the fact that the tutotials used are older and flask has updated by researching online through sources sucre as the flask documentation and stack overflow and other developer groups I was able to reconfiger the model so it will reflect the updated values and attributes 

by using the keycheck.py by 
python keycheck.py 
this will disply how yyour code is being encoded 
open the file to configure with your key

