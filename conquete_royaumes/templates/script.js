const players = [
  { name: "Thomas", role: "admin", points: 0, gold: 0, troops: 5, pixels: 0, eliminated: false },
  { name: "test", role: "player", points: 0, gold: 0, troops: 5, pixels: 0, eliminated: false },
  { name: "Léo", role: "player", points: 0, gold: 0, troops: 5, pixels: 0, eliminated: false }
];

const currentPlayer = players.find(p => p.name === "Thomas"); // remplace "Thomas" par le pseudo admin

if (currentPlayer.role !== "admin") {
  document.getElementById("admin-controls").style.display = "none";
}

function displayPlayers() {
  const container = document.getElementById("players-container");
  container.innerHTML = "";
  players.forEach(player => {
    const div = document.createElement("div");
    div.className = "player";
    div.innerHTML = `
      <h2>${player.name} (${player.role})</h2>
      <p>Points: ${player.points}</p>
      <p>Or: ${player.gold}</p>
      <p>Troupes: ${player.troops}</p>
      <p>Pixels: ${player.pixels}</p>
      <p>${player.eliminated ? "💀 Éliminé" : ""}</p>
    `;
    container.appendChild(div);
  });
}

function resetGame() {
  players.forEach(player => {
    player.points = 0;
    player.gold = 0;
    player.troops = 5;
    player.pixels = 0;
    player.eliminated = false;
  });
  displayPlayers();
}

function boostAdmin() {
  const admin = players.find(p => p.role === "admin");
  if (admin) {
    admin.points += 10;
    admin.gold += 10;
    admin.troops += 100;
    displayPlayers();
  }
}

function startGame() {
  setInterval(() => {
    players.forEach(player => {
      if (!player.eliminated) {
        player.troops += 1;
        checkElimination(player);
      }
    });
    displayPlayers();
  }, 2000);
}

function checkElimination(player) {
  if (player.troops <= 0) {
    player.eliminated = true;
  }
}


displayPlayers();
startGame();
