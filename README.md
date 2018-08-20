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

![alt text](https://raw.githubusercontent.com/para0rmal/jt/master/examples/help.png)

Read JSON from a file:
```
$ jt filename
```

![alt text](https://raw.githubusercontent.com/para0rmal/jt/master/examples/file.png)

Read JSON from GET requestL
```
$ jt -u https://api.github.com/users/para0rmal/repos
```

![alt text](https://raw.githubusercontent.com/para0rmal/jt/master/examples/http_get.png)
