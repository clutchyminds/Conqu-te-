import time

class Game:
    def __init__(self):
        self.players = {}
        self.grid = {}
        self.last_gain_time = {}

        self.couleurs = [
            "#e6194b", "#3cb44b", "#ffe119", "#4363d8",
            "#f58231", "#911eb4", "#46f0f0", "#f032e6",
            "#bcf60c", "#fabebe"
        ]

    def add_player(self, pseudo):
        if pseudo not in self.players:
            couleur = self.couleurs[len(self.players) % len(self.couleurs)]
            self.players[pseudo] = {
                "points": 0,
                "or": 10,
                "troupes": 100,
                "couleur": couleur,
                "nom": pseudo,
                "zone": []
            }
            self.last_gain_time[pseudo] = time.time()

    def get_state_for(self, pseudo):
        joueur = self.players[pseudo]
        now = time.time()
        if now - self.last_gain_time[pseudo] >= 10:
            joueur["troupes"] += 5
            self.last_gain_time[pseudo] = now
        return joueur

    def coloniser(self, pseudo, x, y):
        joueur = self.players[pseudo]
        key = f"{x},{y}"
        owner = self.grid.get(key)

        if owner is None:
            if joueur["troupes"] < 5:
                return "Pas assez de troupes (5 requises)"
            self.grid[key] = pseudo
            joueur["troupes"] -= 5
            joueur["zone"].append(key)
            joueur["points"] += 1
            return "Colonisation réussie"
        elif owner != pseudo:
            if joueur["troupes"] < 20:
                return "Pas assez de troupes pour attaquer (20 requises)"
            self.grid[key] = pseudo
            joueur["troupes"] -= 20
            joueur["points"] += 2
            joueur["zone"].append(key)
            return f"Territoire conquis sur {owner}"
        else:
            return "Ce pixel est déjà à toi"

    def tricher(self, pseudo):
        joueur = self.players[pseudo]
        joueur["troupes"] += 100
        joueur["points"] += 100
        joueur["or"] += 100

    def reset_game(self):
        self.grid.clear()
        for pseudo, joueur in self.players.items():
            joueur["points"] = 0
            joueur["zone"] = []
