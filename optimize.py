import nfl_data_py as nfl
from constants import rosters, cols_and_weights
from utils import compile_player_df, weight_stats, optimize_lineup
# inj = nfl.import_injuries([2023])
# player = inj[inj["full_name"] == "Cooper Kupp"]
# print(player["report_status"])
# exit()
imported_cols = cols_and_weights.keys()
weekly_data = nfl.import_weekly_data(years=[2023])

for team in rosters:
    players = [player for position in rosters[team]["players"] for player in rosters[team]["players"][position]]

    player_positions = rosters[team]["players"].copy()

    player_data = compile_player_df(weekly_data, players, player_positions, imported_cols, cols_and_weights)

    player_data_weighted = weight_stats(player_data)

    optimize_lineup(team, rosters, player_data_weighted)