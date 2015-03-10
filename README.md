# RequestOn
### Create and manage app's services requests with python
RequestOn is a python open source software that allow check the availability of services. It uses [dashy](https://github.com/thoughtworks.com/dashy) as dashboard to show the status of the service.

### Installation  
#### Stable version
[![PyPi version](https://pypip.in/v/requeston/badge.png)](https://pypi.python.org/pypi/requeston)
```ssh
pip install requeston
```
### How to use
```ssh
requestOn -t https://google.com https://github.com https://facebook.com
requestOn -t http://despegar.com http://decolar.com -l log_file.txt
```
###How to contribute:
[![Build Status](https://snap-ci.com/nicolastrres/requestOn/branch/master/build_image)](https://snap-ci.com/nicolastrres/requestOn/branch/master)
[![PyPi downloads](https://pypip.in/d/requeston/badge.png)](https://pypi.python.org/pypi/requeston)
[![Stories in Ready](https://badge.waffle.io/nicolastrres/requestOn.svg?label=ready&title=Ready)](http://waffle.io/nicolastrres/requestOn)

[![Throughput Graph](https://graphs.waffle.io/nicolastrres/requestOn/throughput.svg)](https://waffle.io/nicolastrres/requestOn/metrics)

1. Fork the repository https://github.com/nicolastrres/requestOn/fork
2. Write your tests on tests/test.py
3. Run the tests using the script run_tests.sh, because this is going to run the pep8 too.
4. Push your changes and make a pull request.
5. **All pull requests need to have a crazy picture or a funny video or something that represent that Pull Request. This is the most important! :)**
