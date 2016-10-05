import pytest
from pygraylog.pygraylog import graylogapi

def test_get():
    api = graylogapi.GraylogAPI('http://echo.jsontest.com/one/two', 
        username = 'Zack',
        password = 'Zack')
    res = api._get()
    expected = "{\"one\": \"two\"}\n"
    assert res == expected

def test_post():
    api = graylogapi.GraylogAPI('http://echo.jsontest.com/one/two', 
            username = 'Zack',
            password = 'Zack')
    with pytest.raises(NotImplementedError):
        api._post()

def test_put():
    api = graylogapi.GraylogAPI('http://echo.jsontest.com/one/two', 
            username = 'Zack',
            password = 'Zack')
    with pytest.raises(NotImplementedError):
        api._put()

def test_delete():
    api = graylogapi.GraylogAPI('http://echo.jsontest.com/one/two', 
            username = 'Zack',
            password = 'Zack')
    with pytest.raises(NotImplementedError):
        api._delete()

