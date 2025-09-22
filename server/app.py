from flask import Flask, request
import os
import pathlib

app = Flask(__name__)
app.static_folder = "./static"

@app.route("/")
@app.route("/<path:path>")
def show(path=""):
    new_path = pathlib.Path(app.static_folder, path)
    if new_path.is_file():
        return new_path.open("rb")
    files = list(new_path.glob("*"))
    return_str = ""
    for i in files:
        return_str += f"<a href='{str(i.resolve()).split("static")[-1]}'>{i.name}</a><br>"
    return return_str

@app.route("/<gitsha>", methods=["POST"])
def upload(gitsha: str):
    if(gitsha == None):
        return {}, 204
    
    file = pathlib.Path(app.static_folder, gitsha)

    files = list(file.glob("index_*.html"))
    files.sort(reverse=True)
    num = int(files[0].name.split("_")[-1].split(".html")[0])+1
    
    new_filename = pathlib.Path(file, f"index_{num}.html")
    f = request.files["html_file"]
    f.save(new_filename)



if __name__ == '__main__':
    app.run(debug=True)