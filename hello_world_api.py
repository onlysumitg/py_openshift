from flask import Flask, render_template, request, redirect, url_for

"""
every flask must have a unique name in the project
"""

app = Flask(__name__)  ## __name__  > is always unique for the project


@app.route('/')
def home_page():
    return "hello word"
    #return render_template("homepage.html", posts=posts)



if __name__ == '__main__':
    app.run(debug=True, port=8080)  ##more info in case of error  . .