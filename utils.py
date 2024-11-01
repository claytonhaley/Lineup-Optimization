import pulp


def compile_player_df(weekly_player_data, roster_players, positions, req_cols, cols_and_weights):
    player_data_final = {}

    for p in roster_players:
        player_data = weekly_player_data[weekly_player_data["player_display_name"] == p].copy()
        if len(player_data) == 0:
            # print(f"{p} not available")
            for key in positions.keys():
                if p in positions[key]:
                    positions[key].remove(p)
            continue
    
        player_data.fillna(0.0)
        
        player_data["fumbles_lost"] = player_data["sack_fumbles_lost"] + player_data["rushing_fumbles_lost"] + player_data["receiving_fumbles_lost"]
        player_data["2pt_conversions"] = player_data["passing_2pt_conversions"] + player_data["rushing_2pt_conversions"] + player_data["receiving_2pt_conversions"]

        for col in req_cols:
            player_data[col] = player_data[col] * cols_and_weights[col]

        player_data_reduced = player_data[req_cols].copy()
        
        weekly_data_list = [list(row) for _, row in player_data_reduced.iterrows()]
        
        player_data_final[p] = weekly_data_list

    return player_data_final


def weight_stats(player_data):
    max_len = 0
    for player in player_data:
        if len(player_data[player]) > max_len:
            max_len = len(player_data[player])
        

    for player in player_data:
        if len(player_data[player]) < max_len:
            for _ in range(max_len - len(player_data[player])):
                player_data[player].append([0.0]*len(player_data[player][0]))

    return player_data


def optimize_lineup(team, rosters, player_data_weighted):
    # Compute average past stats
    players_avg_data = {
        player: [sum(stat)/len(stat) for stat in zip(*games)]
        for player, games in player_data_weighted.items()
    }

    # Create the linear programming problem
    prob = pulp.LpProblem("FantasyFootball", pulp.LpMaximize)

    # Decision variables
    player_vars = pulp.LpVariable.dicts("Player", players_avg_data.keys(), 0, 1, pulp.LpBinary)

    # Objective function
    prob += pulp.lpSum([
        player_vars[player] * sum(players_avg_data[player])
        for player in players_avg_data
    ]), "TotalExpectedPoints"

    # Constraints
    qbs = rosters[team]["players"]["QB"]
    rbs = rosters[team]["players"]["RB"]
    wrs = rosters[team]["players"]["WR"]
    tes = rosters[team]["players"]["TE"]

    prob += pulp.lpSum([player_vars[player] for player in qbs]) == rosters[team]["constraints"]["QB"]
    prob += pulp.lpSum([player_vars[player] for player in rbs]) == rosters[team]["constraints"]["RB"]
    prob += pulp.lpSum([player_vars[player] for player in wrs]) == rosters[team]["constraints"]["WR"]
    prob += pulp.lpSum([player_vars[player] for player in tes]) == rosters[team]["constraints"]["TE"]

    # Solve the problem
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # Print the results
    print(f"Selected Players for {team}:\n")
    for player in players_avg_data:
        if player_vars[player].value() == 1:
            print(player)
    print("\n-------------------------------\n")