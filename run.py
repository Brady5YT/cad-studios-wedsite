from flask import Flask, render_template

app = Flask(__name__, template_folder="site", static_folder="site/assets")

@app.route("/")
def home():
    return render_template("index.html")

def main():
    app.run()

if __name__ == "__main__":
    main()