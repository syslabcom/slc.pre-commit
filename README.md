# slc.pre-commit

A collection of generic [pre-commit](https://pre-commit.com/) hooks.

## check-po

Tries to parse `.po` files and reports syntax errors.

```
$ bin/check-po --help
usage: check-po [-h] [filenames [filenames ...]]

positional arguments:
  filenames   Filenames to check.

optional arguments:
  -h, --help  show this help message and exit
```

