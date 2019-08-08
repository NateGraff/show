#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    version_string = '.'.join([str(x) for x in list(sys.version_info)[:3]])

    print(sys.argv[0] + ": Running in Python " + version_string  + " @ " + sys.executable)

