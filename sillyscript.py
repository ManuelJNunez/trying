import os

var = os.getenv('RANDOM_VAR')

print("no")
if var:
    print("Oh, it works!")
else:
    print("Oops, it didn't work.")
