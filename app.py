from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates")

# ✅ In-memory storage (temporary)
contents = []


# ✅ HOME (ADD + VIEW)
@app.route("/", methods=["GET", "POST"])
def home():
    global contents

    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("description")

        if title and desc:
            contents.append([title, desc])

        return redirect("/")

    return render_template("index.html", contents=contents)


# ✅ DELETE
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    global contents

    if id < len(contents):
        contents.pop(id)

    return redirect("/")


# ✅ EDIT
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    global contents

    if id >= len(contents):
        return redirect("/")

    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("description")

        contents[id] = [title, desc]
        return redirect("/")

    return render_template("edit.html", content=contents[id], id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)