[![version](https://img.shields.io/badge/Version-1.0-teal.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-teal.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/para0rmal/jt.svg?branch=master)](https://travis-ci.com/para0rmal/jt)


# jt

jt is a command line utility which allows you to visualise JSON schemas as text trees. It may be used as a complement to `jq`, to facilitate the interpretation of a JSON schema, prior to defining filters.

Note: At this point it assumes consistency across data contained in arrays and only evaluates the schema of the first element.

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

![help](https://user-images.githubusercontent.com/15225347/44439020-c9ebb280-a5b9-11e8-86d0-72b20fc0f01c.png)

Read JSON from a file:
```
$ jt file.json
```

![file](https://user-images.githubusercontent.com/15225347/44439019-c9ebb280-a5b9-11e8-88c4-001169230042.png)

Read JSON from a stream:
```
$ echo '{"node_0": {"node_0_0": [{"node_0_0_0": "", "node_0_0_1": [""]}]}}' | jt -s
```

![stream](https://user-images.githubusercontent.com/15225347/44439021-c9ebb280-a5b9-11e8-8743-a263f3adeb3b.png)

Read JSON from a HTTP GET request:
```
$ jt -u https://api.github.com/users/para0rmal/repos
```

![url](https://user-images.githubusercontent.com/15225347/44439022-c9ebb280-a5b9-11e8-82d1-cd78cce714d2.png)
