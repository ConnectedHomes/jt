[![version](https://img.shields.io/badge/Version-1.0-teal.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-teal.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/para0rmal/jt.svg?branch=master)](https://travis-ci.com/para0rmal/jt)


# jt

jt is a command line utility which allows you to visualise JSON schemas, as ASCII trees.

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

#### A) Virtual Environment Installation

You may use the `pipenv` virtual environment manager from PyPy. 

Install `pipenv`:
```
$ pip3 install pipenv
```

Install `jt` within a virtual environment using `pipenv`:
```
$ pipenv --python 3.6 install -e .
```

Activate the virtualenv (deactivate with `exit`):
```
$ pipenv shell
```


#### B) Local Installation

Install locally:
```
$ python3 setup.py install
```

Examples
---

View help:
``` 
$ jt -h 
```

![help](https://user-images.githubusercontent.com/15225347/44381165-e975d300-a506-11e8-9c67-85bf6dd7bd45.png)

Read JSON from a file:
```
$ jt file.json
```

![file](https://user-images.githubusercontent.com/15225347/44379714-25a53580-a4ff-11e8-8a7b-b5dd87046f89.png)

Read JSON from a stream:
```
$ echo '{"node_0": {"node_0_0": [{"node_0_0_0": "", "node_0_0_1": [""]}]}}' | jt -s
```

![stream](https://user-images.githubusercontent.com/15225347/44379717-25a53580-a4ff-11e8-9cd4-ef90c1f02a76.png)

Read JSON from a HTTP GET request:
```
$ jt -u https://api.github.com/users/para0rmal/repos
```

![url](https://user-images.githubusercontent.com/15225347/44379718-263dcc00-a4ff-11e8-8bc6-dbdbd20c2400.png)
