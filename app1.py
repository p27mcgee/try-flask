from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bam!</h1>"

@app.route("/<chum>")
def user(chum):
    return f"Hello, {chum}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/ynh")
def yours():
    return redirect(url_for("user", chum="Baby Boy"))

@app.route("/oogah")
def render_index():
    return render_template("index.html", content="Right here!")

if __name__ == "__main__":
    app.run(debug=True)