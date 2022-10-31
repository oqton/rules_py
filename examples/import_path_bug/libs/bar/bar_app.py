import json
import sys

print(json.dumps(sys.path, indent=2))

from libs.foo import foo_lib

foo_lib.print_foo()
