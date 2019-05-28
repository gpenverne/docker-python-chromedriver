# docker-python-chromedriver

Python with Chromedriver, for running automated tests from [https://github.com/joyzoursky/docker-python-chromedriver](https://github.com/joyzoursky/docker-python-chromedriver). I just added sudo for my own usage (and some python3 libraries)

## Includes:

 - Python
 - Google Chrome
 - Chromedriver

## Versions:

### Python 3:

 - `3.7` (based on python:3.7, [Dockerfile](https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py3/py3.7/Dockerfile))

## Usage:


For the following ubuntu based images:
- `3.7`


Run the followings in your terminal:

```
$ cd [your working directory]
$ docker run -it -w /usr/workspace -v $(pwd):/usr/workspace gpenverne/python-chromedriver:[version] bash
```
