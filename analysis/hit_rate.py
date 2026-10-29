"""Analyze fictional player data. No APIs or external packages required."""

import csv
from datetime import date
from pathlib import Path

# Explicit settings make the analysis reproducible.
PLAYER_ID = "P001"
STATISTIC = "points"
THRESHOLD = 20.5
WINDOW = 6
CUTOFF = date(2026, 10, 28)

# Find the CSV relative to this script, regardless of the working directory.
DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "synthetic_player_games.csv"
)


def main():
    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    # One observation should exist per player, game, and statistic.
    unique = {}
    duplicates = 0

    for row in rows:
        if row["player_id"] != PLAYER_ID or row["statistic"] != STATISTIC:
            continue

        key = (row["player_id"], row["game_id"], row["statistic"])

        if key in unique:
            if row == unique[key]:
                duplicates += 1
                continue
            raise ValueError(f"Conflicting records for {key}; review required.")

        unique[key] = row

    eligible = [
        row
        for row in unique.values()
        if row["game_status"] == "completed"
        and row["participation_status"] == "played"
        and date.fromisoformat(row["game_date"]) < CUTOFF
    ]

    # ISO dates sort chronologically. Game ID breaks ties consistently.
    eligible.sort(
        key=lambda row: (row["game_date"], row["game_id"]),
        reverse=True,
    )
    selected = eligible[:WINDOW]

    print(f"Source rows: {len(rows)}")
    print(f"Identical duplicates removed: {duplicates}")
    print(f"Selected games: {len(selected)} of {WINDOW} requested")

    if not selected:
        print("Insufficient data: no eligible games.")
        return

    # Validate after choosing the window; never silently backfill older games.
    values = []
    for row in selected:
        try:
            value = float(row["value"])
        except (ValueError, TypeError):
            raise ValueError(
                f"Missing or invalid value for {row['game_id']}; review required."
            ) from None

        # Also rejects NaN and infinity for this counting statistic.
        if not (0 <= value < float("inf")) or not value.is_integer():
            raise ValueError(
                f"Invalid points value for {row['game_id']}; review required."
            )

        values.append(value)

    hits = sum(value > THRESHOLD for value in values)
    hit_rate = hits / len(values) * 100

    print(f"Games above {THRESHOLD}: {hits} of {len(values)}")
    print(f"Historical hit rate: {hit_rate:.1f}%")
    print("Synthetic historical sample; not a prediction.")


if __name__ == "__main__":
    main()
