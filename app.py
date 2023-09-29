from flask import Flask, render_template, request, redirect, session
from bin import interface

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return render_template("verify-page.html")

@app.route("/process", 
           methods=["POST"])
def process_input():
    choice = request.form["inputchoice"]
    if choice=="link":
        inp = request.form["inp-link"]        
    elif choice=="forward":
        inp = request.form["inp-text"]
    
    res = interface.news_ops(inp, choice)
    if res == None:
        return redirect("/verification-failed")
    session["response"] = res
    return redirect("/verification-success")

@app.route("/verification-failed")
def failed():
    return render_template("failure.html")

@app.route("/verification-success")
def success():
    return render_template("results.html", 
                           res=session["response"])

if __name__ == "__main__":
    app.run()