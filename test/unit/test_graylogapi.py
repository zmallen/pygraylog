import pytest
import base64
from pygraylog.pygraylog import graylogapi

def test_obj_creation():
    # test based on username / password API end-point access level
    api = graylogapi.GraylogAPI('https://test.com/foo/bar/',
        username = 'Zack',
        password = 'Zack',
        api_key = None)
    assert api._path == '/foo/bar/'
    assert api.username == 'Zack'
    assert api.password == 'Zack'
    assert api.api_key is None
    
    # test based on api-key token access level
    api = graylogapi.GraylogAPI('https://test.com/foo/bar/',
        username = None,
        password = None,
        api_key = 'ABCDEFG')
    assert api._path == '/foo/bar/'
    assert api.username is None
    assert api.password is None
    assert api.api_key == 'ABCDEFG'    

def test_obj_path_build():
    api = graylogapi.GraylogAPI('https://test.com')
    assert api._path == ''
    api = api.foo
    assert api._path == '/foo'
    api = api.bar.baz
    assert api._path == '/foo/bar/baz'
    api = api._('from')
    assert api._path == '/foo/bar/baz/from'

def test_auth_header():
    # test based on username / password API end-point access level
    api = graylogapi.GraylogAPI('/',  username='Zack', password='Zack')
    header = api.build_auth_header()
    payload = 'Zack' + ':' + 'Zack' 
    header_test = {
        'Authorization' : 'Basic ' + base64.b64encode(payload),
        'Accept' : 'application/json'
    }
    assert header == header_test
    
    # test based on api-key token access level
    api = graylogapi.GraylogAPI('/',
        username = None,
        password = None,
        api_key = 'ABCDEFG')
    header = api.build_auth_header()
    payload = 'ABCDEFG' + ':' + 'token'
    header_test = {
        'Authorization' : 'Basic ' + base64.b64encode(payload),
        'Accept' : 'application/json'
    }
    assert header == header_test
