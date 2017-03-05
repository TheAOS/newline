# newline
Python 2.7 script and module for adding newline to end of files, with recursive search

## Notes
`PATTERN` should be regex

## Usage
```
usage: newlines.py [-h] [-r] [-v] [-c] [-p PATTERN] path

positional arguments:
  path                  path to file/dir

optional arguments:
  -h, --help            show this help message and exit
  -r, -R, --recurse     recursive search
  -v, -V, --verbose     verbose output, tells you what it's done
  -c, -C, --confirm     confirms changes automatically
  -p PATTERN, -P PATTERN, --pattern PATTERN
                        regex for file matching (python style)
```
