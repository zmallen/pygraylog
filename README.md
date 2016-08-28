# pygraylog - API Wrapper for Graylog 2.0

[![Build Status](https://travis-ci.org/zmallen/pygraylog.svg?branch=zma%2Fadd_tests)](https://travis-ci.org/zmallen/pygraylog)

The purpose of this code is to provide a lightweight wrapper to GraylogAPI. It provides standard access to the Graylog 2.0 API endpoints, and it will tell you if you are missing a specific field when calling it. 

## Usage

Install this library, then import the GraylogAPI class.

`import pygraylog.GraylogAPI`

Then, make an object with your base Graylog URL and username and password for auth

`api = pygraylog.GraylogAPI('https://localhost:12900', username='foo', password='foo')`

Then, check out `pygraylog/endpoints.py` to see which endpoints are implemented/enforced by this library and make your API call.

`api.search.universal.absolute(fields="src_ip", query="*", from_='1970-01-01 00:00:00', to='1970-01-01 23:59:59')`  

Notice that each argument here is listed in `endpoints.py` as required,  but you can pass in as many as you want (limit, offset, filter for example) and `pygraylog` will send it for you.

## Installation

### Development

* Clone this repo
* `cd /path/to/pygraylog`
* `virtualnenv env`
* `. env/bin/activate`
* `pip install -r requirements.txt`

### As a library
* `pip install pygraylog` 
* `import pygraylog.GraylogAPI`
