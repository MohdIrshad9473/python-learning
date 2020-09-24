from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello")
    return 'Hello, World!'

# This is an option to start server lekin use nhi karte
# if __name__ =="__main__":
#   app.run(host="localhost", port=8000, debug=True)

# 1. to stop Flask Applica+tion  Ctlr + C
# 2. Already told you  about Enviournment Variables
# Btter Approach to start server 
#  set FLASK_APP=main.py
#  flask run

