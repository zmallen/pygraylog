import pytest
import base64
from pygraylog.pygraylog import graylogapi

def test_obj_creation():
    api = graylogapi.GraylogAPI('https://test.com/foo/bar/',
        username = 'Zack',
        password = 'Zack',
        api_key = 'ABCDEFG')
    assert api._path == '/foo/bar/'
    assert api.username == 'Zack'
    assert api.password == 'Zack'
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
    api = graylogapi.GraylogAPI('/',  username='Zack', password='Zack')
    header = api.build_auth_header()
    payload = 'Zack' + ':' + 'Zack' 
    header_test = {
        'Authorization': 'Basic ' + base64.b64encode(payload)
    }
    assert header == header_test
