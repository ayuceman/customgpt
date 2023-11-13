from isapi_wsgi import WSGIServer

def __ExtensionFactory__():
    from app import app  # Replace 'yourapp' with your actual Flask app module
    return WSGIServer(app)
