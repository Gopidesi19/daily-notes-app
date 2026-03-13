from flask import Flask, render_template, request, redirect
from google.cloud import firestore
import datetime

app = Flask(__name__)
db = firestore.Client()

@app.route("/")
def index():
    notes_ref = db.collection("notes")
    docs = notes_ref.order_by("timestamp").stream()
    notes = []
    for doc in docs:
        notes.append(doc.to_dict())
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    note_text = request.form.get("note")
    if note_text:
        db.collection("notes").add({
            "note": note_text,
            "timestamp": datetime.datetime.utcnow()
        })
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)