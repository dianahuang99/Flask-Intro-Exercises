# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div


app = Flask(__name__)


@app.route("/<op>")
def calculate(op):
    if op == "add":
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(add(a, b))
    elif op == "sub":
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(sub(a, b))
    elif op == "mult":
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(mult(a, b))
    elif op == "div":
        a = int(request.args["a"])
        b = int(request.args["b"])
        return str(int(div(a, b)))


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
