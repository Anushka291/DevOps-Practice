import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "content.txt")

# ensure directories exist
os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)

# create file if missing
if not os.path.exists(DATA_FILE):
    open(DATA_FILE, "w").close()

print("DATA FILE PATH:", DATA_FILE)

def read_contents():
    contents = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                parts = line.split("|")
                if len(parts) >= 2:
                    contents.append(parts)
    return contents


def write_contents(contents):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for c in contents:
            f.write("|".join(c) + "\n")


# ✅ HOME (ADD + VIEW)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("description")

        if title and desc:
            with open(DATA_FILE, "a", encoding="utf-8") as f:
                f.write(f"{title}|{desc}\n")

        return redirect("/")

    contents = read_contents()
    return render_template("index.html", contents=contents)


# ✅ DELETE
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    contents = read_contents()

    if id < len(contents):
        contents.pop(id)
        write_contents(contents)

    return redirect("/")


# ✅ EDIT
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    contents = read_contents()

    if id >= len(contents):
        return redirect("/")

    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("description")

        contents[id] = [title, desc]
        write_contents(contents)

        return redirect("/")

    return render_template("edit.html", content=contents[id], id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)