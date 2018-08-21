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

![help](https://user-images.githubusercontent.com/15225347/44377839-6056a000-a4f6-11e8-9af1-956fc3867bcc.png)

Read JSON from a file:
```
$ jt file.json
```

![file](https://user-images.githubusercontent.com/15225347/44377838-6056a000-a4f6-11e8-810e-f61f06a31255.png)

Read JSON from a stream:
```
$ echo '{"node_0": {"node_0_0": [{"node_0_0_0": "", "node_0_0_1": [""]}]}}' | jt -s
```

![stream](https://user-images.githubusercontent.com/15225347/44377840-6056a000-a4f6-11e8-8347-9376f5bed692.png)

Read JSON from GET request:
```
$ jt -u https://api.github.com/users/para0rmal/repos
```

![url](https://user-images.githubusercontent.com/15225347/44377934-c9d6ae80-a4f6-11e8-9b98-a678a4aae050.png)
