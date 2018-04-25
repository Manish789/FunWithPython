# Generating the hash for a file ( using md5 ).
# Taking the filename as argument while running the script.

import hashlib
import sys
file_name = sys.argv[1]
read_file = open(file_name)
the_hash = hashlib.md5()
for line in read_file.readlines():
    the_hash.update(line.encode('utf-8'))
print(the_hash.hexdigest())
