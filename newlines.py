""" Module that ensures newlines at EOF in path matching regex """

import os.path
import os
import re

def ensure_newline(path, verbose=False):
    """ Ensures newline at EOF """
    if not has_newline(path, verbose):
        add_newline(path, verbose)

def add_newline(path, verbose=False):
    """ Adds newline at EOF """
    if os.path.isfile(path):
        current_file = file(path, 'a')
        current_file.write('\n')
        if verbose:
            print "Added newline to: %s" % path
        current_file.close()
    else:
        raise IOError("%s is not a file" % path)

def has_newline(path, verbose=False):
    """ Checks if newline at EOF """
    if os.path.isfile(path):
        current_file = file(path, 'r')
        current_file.seek(-1, 2)
        newline = current_file.read(1) == '\n'
        current_file.close()
        if verbose:
            print "%s has newline: %s" % (path, newline)
        return newline
    else:
        raise IOError("%s is not a file" % path)

def _find_files(path, regex, recurse, verbose, files):
    if os.path.isdir(path):
        dir_list = os.listdir(path)
        for pos in dir_list:
            next_path = os.path.join(path, pos)
            if os.path.isfile(next_path):
                match = regex.match(pos)
                if match is not None and not has_newline(next_path, verbose):
                    files.append(next_path)
            elif os.path.isdir(next_path) and recurse:
                _find_files(next_path, regex, recurse, verbose, files)

def ensure_newlines(path, regex, recurse=False, verbose=False, confirm=False):
    """ Ensures newlines at EOF in path matching regex """
    regex = re.compile(regex)
    if os.path.isdir(path):
        file_list = []
        _find_files(path, regex, recurse, verbose, file_list)
        if not confirm:
            if len(file_list) == 0:
                print "No files without newline found"
                return
            for pos in file_list:
                print pos
            while True:
                confirmed = raw_input("Do you want to add newlines to ALL the above files? Y/N\n")
                if confirmed in "nN":
                    return
                if confirmed in "yY":
                    break
        for pos in file_list:
            add_newline(pos, verbose)
    elif os.path.isfile(path):
        ensure_newline(path, verbose)
    else:
        raise IOError("No directory or file at location")

def _main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "-R", "--recurse",
                        help="recursive search", action="store_true")
    parser.add_argument("-v", "-V", "--verbose",
                        help="verbose output, tells you what it's done", action="store_true")
    parser.add_argument("-c", "-C", "--confirm",
                        help="confirms changes automatically", action="store_true")
    parser.add_argument("-p", "-P", "--pattern",
                        help="regex for file matching (python style)")
    parser.add_argument("path",
                        help="path to file/dir")
    args = parser.parse_args()
    ensure_newlines(args.path, args.pattern, args.recurse, args.verbose, args.confirm)

if __name__ == "__main__":
    _main()
