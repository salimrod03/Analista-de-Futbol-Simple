# Main Flask application
# Proyecto: Analista de Fútbol
# Estructura recomendada por Cursor AI

from flask import Flask, render_template
from data.partidos import partidos

app = Flask(__name__)


def calculate_stats():
    total_matches = len(partidos)
    total_goals = 0
    home_wins = 0
    draws = 0
    away_wins = 0

    for match in partidos:
        total_goals += match["home_goals"] + match["away_goals"]

        if match["home_goals"] > match["away_goals"]:
            home_wins += 1
        elif match["home_goals"] < match["away_goals"]:
            away_wins += 1
        else:
            draws += 1

    avg_goals = round(total_goals / total_matches, 2)

    probabilities = {
        "local": round(home_wins / total_matches * 100, 2),
        "empate": round(draws / total_matches * 100, 2),
        "visita": round(away_wins / total_matches * 100, 2),
    }

    return {
        "total": total_matches,
        "promedio_goles": avg_goals,
        "home_wins": home_wins,
        "draws": draws,
        "away_wins": away_wins,
        "probabilities": probabilities
    }


@app.route("/")
def index():
    return render_template("index.html", partidos=partidos)


@app.route("/stats")
def stats():
    stats_data = calculate_stats()
    return render_template("stats.html", stats=stats_data)


if __name__ == "__main__":
    app.run(debug=True)
