import subprocess

subprocess.check_call('py/tests/binary_calls_binary/first/first', env={'FOO': 'bar'})
