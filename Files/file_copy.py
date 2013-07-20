# File Copy Utility
# Create a utility that can do bulk file copying and backups of other files.

"""
For now it just copies a file
"""

import sys

program, original, copy = sys.argv

fin = open(original)
fout = open(copy, "w")

fout.write(fin.read())

fin.close()
fout.close()