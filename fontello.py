#!/usr/bin/env python3.7
import re
import sys

cssFile = open( sys.argv[1], 'r' )
cssContent = cssFile.read()

cssLines = re.split("\n+", cssContent)
items = [];
for cssLine in cssLines:
    pattern = re.compile("^.i-([^:]+):before\s*{\s*content:\s*([^;]+);")
    matched = re.match( pattern, cssLine )

    if matched:
        items.append( matched.group(1) + ': '+ matched.group(2) )

print( '\n\n' )
print( ',\n'.join(items) )
print( '\n\n' )
