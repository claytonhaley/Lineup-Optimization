# Lineup-Optimization

This repository consists of two separate projects:

1. Optimizing fantasy football lineups
2. Simulating player performance to make weekly fantasy football point projections

**NOTE** Both this project and the simulation project require some manual data collection, which can be time consuming.

## Otimizing Lineups
This project utilizes the PuLP library for linear optimization. It takes weekly data for a select group of players, and solves for the optimial lineup for that specific week.

In `constants.py` there is a variable called `rosters`. Each roster contains the players and their respective roster constraints (Max number of players at each position). There is also a variable called `cols_and_weights` that constains the weights for each fantasy football statistic. Please fill these variables for your respective leagues.

Run the following command to run optimizations:
```bash
python3 optimize.py
```

## Player Point Projections
This project performs monte carlo simulations for each player, taking random samples for each relevant fantasy footbalol statistic. It will output a `.csv` file with the following statistics:

- player
- position
- mean_fantasy_points
- stddev
- floor
- ceiling
- expected_model

It will also output a plot comparing std dev and the expected points, displaying the consistency of each player.

There are two steps to run this:

1. Create a `.txt` file with player metadata
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
```bash
python3 mc_sim.py
```

