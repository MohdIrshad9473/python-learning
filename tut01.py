# enviournmnet variables are use to have security
# each to change variables in other server ( dev ,  testing, production )
# Instruction documnet - readme.md

import os

# set enviournmnet variable
email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

print(email,password)