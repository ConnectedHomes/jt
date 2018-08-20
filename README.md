# jt

jt is a command line utility which allows you to visualise the nodes in a JSON file (or GET request) as an asciitree.

Installation
---
```
$ python3 setup.py install
```

Examples
---

To display help, run:
``` 
$ jt -h 
```

Read JSON from a file:
```
$ jt filename
```

Read JSON from GET requestL
```
$ jt -u https://api.github.com/users/para0rmal/repos
```

