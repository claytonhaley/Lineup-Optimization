# Lineup-Optimization

This repository consists of two separate projects:

1. Optimizing fantasy football lineups
2. Simulating player performance to make weekly fantasy football point projections

**NOTE** Both this project and the simulation project require some manual data collection, which can be time consuming.

## Otimizing Lineups
This project utilizes the PuLP library for linear optimization. It takes weekly data for a select group of players, and solves for the optimial lineup for that specific week.

In `constants.py` there is a variable called `rosters`. Each roster contains the players and their respective roster constraints (Max number of players at each position). There is also a variable called `cols_and_weights` that constains the weights for each fantasy football statistic. Please fill these variables for your respective leagues.

1. Set up your virtual environment
```shell
python3 -m venv optimize
source optimize/bin/activate
```

2. Run the following command to run optimizations:
```shell
python3 optimize.py
```

## Player Point Projections
This project performs monte carlo simulations for each player, taking random samples for each relevant fantasy footbalol statistic. It will output a `results.csv` file with the following statistics:

- player
- position
- mean_fantasy_points
- stddev
- floor
- ceiling
- expected_model

It will also output a plot `risk_vs_reward.html` comparing std dev and the expected points, displaying the consistency of each player.

There are two steps to run this:

1. Create a `players.txt` file with player metadata
```text
Lamar Jackson,BAL,QB
Jared Goff,DET,QB
Bijan Robinson,ATL,RB
James Cook,BUF,RB
Blake Corum,LA,RB
Jaylen Warren,PIT,RB
Tyjae Spears,TEN,RB
...
```

2. Run the program:
```shell
python3 mc_sim.py
```

