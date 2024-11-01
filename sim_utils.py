import csv
import numpy as np
from scipy.stats import norm
import plotly.express as px
from constants import COLS_AND_WEIGHTS


def run_simulation(data, n_iter=10000):
    fantasy_stats = COLS_AND_WEIGHTS["fantasy_stats"]
    non_fantasy_stats = COLS_AND_WEIGHTS["non_fantasy_stats"]

    all_stats = {**fantasy_stats, **non_fantasy_stats}
    final_data = {}
    for i in range(n_iter):
        score = 0
        final_data[f"sim_{i}"] = {}
        for stat in all_stats:
            if len(data[stat]) == 1:
                # Estimate mu (mean) and sigma (standard deviation)
                data_mean = data[stat].iloc[0] / 2  # Midpoint of the range
                data_std = (
                    data[stat].iloc[0] / 4
                )  # Approximate standard deviation using the range rule
            else:
                data_mean = data[stat].mean()
                data_std = data[stat].std()

            if all_stats[stat]["dist_type"] == "poisson":
                rand_var = np.random.poisson(lam=data_mean if data_mean > 0 else 0)
            elif all_stats[stat]["dist_type"] == "normal":
                rand_var = np.random.normal(
                    loc=data_mean if data_mean > 0 else 0,
                    scale=data_std if data_std > 0 else 0,
                )

            if stat in fantasy_stats:
                score += rand_var * fantasy_stats[stat]["weight"]

            final_data[f"sim_{i}"][stat] = rand_var

        final_data[f"sim_{i}"]["fantasy_points"] = score

    return final_data


def summarize(data, player, pos):
    f_points = np.array([data[k]["fantasy_points"] for k in data])
    mean_f_points = np.mean(f_points)
    median_f_points = np.median(f_points)
    std_dev = np.std(f_points)
    percentile_10 = np.percentile(f_points, 10)
    percentile_90 = np.percentile(f_points, 90)

    return {
        "player": player,
        "position": pos,
        "mean_fantasy_points": mean_f_points,
        "stddev": std_dev,
        "floor": percentile_10,
        "ceiling": percentile_90,
        "expected_model": median_f_points,
    }


def expected_vs_risk(data):
    fig = px.scatter(
        data,
        x="expected_points",
        y="stddev",
        color="position",
        hover_name="player",
        title="Player Risk vs Reward Comps",
        labels={"x": "Expected Fantasy Points", "y": "Standard Deviation (Risk)"},
    )

    # Save the plot to an HTML file
    fig.write_html("risk_vs_reward.html")


def write_data(summary_data: dict):
    summary_data
    with open("results.csv", "w", newline="") as csvfile:
        fieldnames = summary_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_data)
