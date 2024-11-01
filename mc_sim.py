import time
import traceback
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import nfl_data_py as nfl
from numpy.core.numeric import full

from sim_utils import run_simulation, summarize, expected_vs_risk, write_data


def run_sim(weekly_data, player):
    try:
        player_name, team, pos = player
        print(f"Running sim for {player_name} ({team})")

        sim_data = weekly_data[weekly_data["player_display_name"] == player_name]
    except:
        print(f"Player {player_name} ({team}) not available. Generating New Data...")

        position_data = weekly_data[weekly_data["position"] == pos]
        team_data = position_data[position_data["recent_team"] == team]

        sim_data = team_data

    sim_results = run_simulation(sim_data)

    summary_data = summarize(sim_results, player_name, pos)
    print(f"Player {player_name} complete")

    return summary_data


if __name__ == "__main__":
    with open("players.txt", "r") as f:
        players = [tuple(line.strip().split(",")) for line in f]

    unique_players = list(map(tuple, set(map(tuple, players))))

    full_weekly_data = nfl.import_weekly_data(years=[2023, 2024])
    full_weekly_data = full_weekly_data.fillna(0.0)

    with ThreadPoolExecutor(max_workers=5) as exe:
        results = exe.map(
            run_sim, [full_weekly_data] * len(unique_players), unique_players
        )

    plot_data = {
        "player": [],
        "position": [],
        "expected_points": [],
        "stddev": [],
    }
    csv_data = []
    for result in results:
        if result is not None:
            plot_data["player"].append(result["player"])
            plot_data["position"].append(result["position"])
            plot_data["expected_points"].append(result["expected_model"])
            plot_data["stddev"].append(result["stddev"])

            csv_data.append(result)

    write_data(csv_data)

    expected_vs_risk(plot_data)
