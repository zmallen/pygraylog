import base64
import requests
from endpoints import endpoints
from urlparse import urlparse
class GraylogAPI(object):
    def __init__(self, url, username=None, password=None, api_key=None):
        self.url = url
        self._path = urlparse(self.url).path
        self.username = username
        self.password = password
        self.api_key = api_key
        self.methods = {
            'get':      self._get, 
            'post':     self._post,
            'put':      self._put,
            'delete':   self._delete
        }

    def _(self, name):
        url = self.url + '/' + name
        return GraylogAPI(url, username=self.username, password=self.password,
            api_key=self.api_key)

    def __getattr__(self, name):
        if name in self.methods.keys():
            def method(**kwargs):
                res = self.call(name, **kwargs)
                return res
            return method
        else:
            return self._(name)

    def build_auth_header(self):
        payload = self.username + ':' + self.password
        header = {
            'Authorization' : 'Basic ' + base64.b64encode(payload),
            'Accept' : 'application/json'
        }
        return header

    def _get(self, **kwargs):
        headers = self.build_auth_header()
        r = requests.get(self.url, params=kwargs, headers=headers)

        return r.text


    def _post(self, **kwargs):
        raise NotImplementedError('POST not implemented')
        
    def _put(self, **kwargs):
        raise NotImplementedError('PUT not implemented')
    
    def _delete(self, **kwargs):
        raise NotImplementedError('DELETE not implemented')

    def call(self, method, **kwargs):
        arg_names = kwargs.keys()
        required_args = endpoints[self._path]
        if not set(required_args).issubset(set(arg_names)):
            raise ValueError(('Not all required arguments passed for %s.\n' +
                'Given: %s\nRequired: %s') 
                % (self._path, arg_names, required_args))
        for arg in required_args:
            if arg in kwargs and arg[-1] == '_':
                kwargs[arg[:-1]] = kwargs.pop(arg)
        res = self.methods[method](**kwargs)
        return res
