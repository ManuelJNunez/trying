import os

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

var = os.getenv('RANDOM_VAR')

if var:
    print("Oh, it works!")
else:
    print("Oops, it didn't work.")
