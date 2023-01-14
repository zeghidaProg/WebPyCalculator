from flask import Flask,  render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcom to the home page"

@app.route("/Page2")
def viewPage2():
    return "see Page2"

@app.route("/About")
def viewContact():
    return "About"

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return "Thanks for your email" 

    else:
        return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True)
