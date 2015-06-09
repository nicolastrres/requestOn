# RequestOn
### Create and manage app's services requests with python
RequestOn is a python open source software that allow check the availability of services. It uses [dashy](https://github.com/thoughtworks.com/dashy) as dashboard to show the status of the service.

## Installation  
##### Stable version 
[![PyPi version](https://img.shields.io/pypi/v/requeston.svg)](https://pypi.python.org/pypi/requeston)

```ssh
pip install requeston
```
## How to use
[![Documentation Status](https://readthedocs.org/projects/requeston/badge/?version=latest)](https://readthedocs.org/projects/requeston/?badge=latest)

You can send the end points from the command line:
```ssh
requestOn -t https://google.com https://github.com https://facebook.com
requestOn -t http://despegar.com http://decolar.com
```
Or you can read them from a file:
```ssh
requestOn -f file_to_read.txt
```
The structure of the file should be:
```ssh
https://google.com
https://github.com
```
## Integration with Dashy
#### How to install 
You can follow the [instructions](https://github.com/thoughtworks/dashy#installation) to install.
Then open a browser and take the app_id of dashy
#### Integrate dashy with requestOn
```ssh 
requestOn -t https://google.com https://github.com -a [APP_ID] -n [APP_NAME]
```
The app name can be anything.
##How to contribute:
[![Build Status](https://snap-ci.com/nicolastrres/requestOn/branch/master/build_image)](https://snap-ci.com/nicolastrres/requestOn/branch/master)
[![PyPi downloads](https://pypip.in/d/requeston/badge.png)](https://pypi.python.org/pypi/requeston)
[![Stories in Ready](https://badge.waffle.io/nicolastrres/requestOn.svg?label=ready&title=Ready)](http://waffle.io/nicolastrres/requestOn)

[![Throughput Graph](https://graphs.waffle.io/nicolastrres/requestOn/throughput.svg)](https://waffle.io/nicolastrres/requestOn/metrics)

1. Fork the repository https://github.com/nicolastrres/requestOn/fork
2. Write your tests on tests/
3. Run the tests using the script run_tests.sh, because this is going to run the pep8 too.
4. Push your changes and make a pull request.
5. **All pull requests need to have a crazy picture or a funny video or something that represent that Pull Request. This is the most important! :)**

##License 
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

The MIT License (MIT)

Copyright (c) 2015 Nicolas Agustin Torres, https://github.com/nicolastrres

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
