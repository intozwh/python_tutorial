from flask import Flask

zwhapp=Flask(__name__)
@zwhapp.route("/")
def hello_world():
    return "<p>hello, world!</p></br>"

@zwhapp.route("/zwh/")
def zwhtest():
    return "<p>this is a zwhtest page.</p></br>"
