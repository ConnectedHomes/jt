[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Build Status](https://travis-ci.com/para0rmal/jt.svg?branch=master)](https://travis-ci.com/para0rmal/jt)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)


# jt

jt is a command line utility which allows you to visualise the nodes in a JSON file (or GET request) as an ASCII tree.

Installation
---


Clone the repository:
```
$ git clone https://github.com/para0rmal/jt.git
```

Enter directory:
```
$ cd jt/
```

##### A) Virtual Environment install.

To install inside a virtual environment you may use:
```
$ pipenv --python 3.6 install -e
```

To activate the virtualenv:
```
$ pipenv shell
```

##### B) Local install.

To install locally:
```
$ python3 setup.py install
```

Examples
---

To display help, run:
``` 
$ jt -h 
```

![help](https://user-images.githubusercontent.com/15225347/44353777-fad7c480-a49f-11e8-9879-7e1bbb39a8d2.png)

Read JSON from a file:
```
$ jt file.json
```

![file](https://user-images.githubusercontent.com/15225347/44353776-fa3f2e00-a49f-11e8-8ac3-7cfaf05e2d46.png)

Read JSON from GET request:
```
$ jt -u https://api.github.com/users/para0rmal/repos
```

![https_get](https://user-images.githubusercontent.com/15225347/44353778-fad7c480-a49f-11e8-8963-80b8eb4a6de8.png)
