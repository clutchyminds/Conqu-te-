from flask import Flask, render_template, request, session, redirect, jsonify
from game import Game

app = Flask(__name__)
app.secret_key = "supersecretkey"
game = Game()

# ✔ Connexion
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pseudo = request.form["pseudo"]
        role = request.form.get("role", "player")
        session["pseudo"] = pseudo
        session["role"] = role
        game.add_player(pseudo)
        return redirect("/grid")
    return render_template("login.html")

# ✔ Inscription
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        pseudo = request.form["pseudo"]
        password = request.form["password"]  # Non vérifié pour l'instant
        session["pseudo"] = pseudo
        session["role"] = "player"
        game.add_player(pseudo)
        return redirect("/grid")
    return render_template("signup.html")

# ✔ Grille
@app.route("/grid")
def grid():
    pseudo = session.get("pseudo")
    if not pseudo:
        return redirect("/login")
    state = game.get_state_for(pseudo)
    role = session.get("role")
    return render_template("grid.html", state=state, game=game, role=role)

# ✔ Coloniser un pixel
@app.route("/pixel", methods=["POST"])
def pixel():
    data = request.get_json()
    pseudo = session.get("pseudo")
    x = data["x"]
    y = data["y"]
    message = game.coloniser(pseudo, x, y)
    return jsonify({"message": message})

# ✔ Tricher
@app.route("/triche", methods=["POST"])
def triche():
    if session.get("role") == "admin":
        pseudo = session.get("pseudo")
        game.tricher(pseudo)
    return redirect("/grid")

# ✔ Réinitialiser la carte
@app.route("/reset", methods=["POST"])
def reset():
    if session.get("role") == "admin":
        game.reset_game()
    return redirect("/grid")

# ✔ Lancer le serveur sur l'IP locale
if __name__ == "__main__":
    app.run(host="192.168.1.126", port=5000, debug=True)
