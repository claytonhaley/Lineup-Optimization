rosters = {
    "Beta Not Be Last": {
        "players": {
            "QB": [
                "Justin Fields",
                "Jared Goff"
            ],
            "RB": [
                "Nick Chubb", 
                "Kenneth Walker",
                "Isiah Pacheco",
                "Jerick McKinnon",
                "Raheem Mostert",
                "Duece Vaughn",
            ],
            "WR": [
                "Davante Adams",
                "Tyler Lockett",
                "Treylon Burks",
                "Skyy Moore",
                "Rashid Shadeed"
            ],
            "TE": [
                "Tyler Higbee",
                "Juwan Johnson"
            ]
        },
        "constraints": {
            "QB": 1,
            "RB": 3,
            "WR": 3,
            "TE": 1
        }
    },
    "Seaside": {
        "players": {
            "QB": [
                "Jalen Hurts",
                "Kyler Murray"
            ],
            "RB": [
                "Josh Jacobs",
                "Travis Etienne",
                "Khalil Herbert",
                "Gus Edwards"
            ],
            "WR": [
                "Tyler Lockett",
                "Christian Kirk",
                "Treylon Burks",
                # "Cooper Kupp",
                "JuJu Smith-Schuster",
                "Rondale Moore"
            ],
            "TE": [
                "Juwan Johnson",
                "George Kittle"
            ]
        },
        "constraints": {
            "QB": 1,
            "RB": 2,
            "WR": 3,
            "TE": 1
        }
    },
    "The Ex-XFL": {
        "players": {
            "QB": [
                "Jalen Hurts",
                "Trevor Lawrence",
            ],
            "RB": [
                "Najee Harris",
                "Nick Chubb",
                "Isiah Pacheco",
                "Samaje Perine",
                "Tyler Allgeier"
            ],
            "WR": [
                "Tyler Lockett",
                "Jaylen Waddle",
                "Christian Kirk",
                "Zay Flowers",
                "Puka Nacua",
            ],
            "TE": [
                "Kyle Pitts",
                "Tyler Higbee"
            ]
        },
        "constraints": {
            "QB": 2,
            "RB": 2,
            "WR": 2,
            "TE": 1
        }
    }
}  


cols_and_weights = {
    'passing_yards': 0.04,
    'passing_tds': 4,
    'interceptions': -2,
    'fumbles_lost': -2, 
    '2pt_conversions': 2,
    'rushing_yards': 0.1,
    'rushing_tds': 6,
    'receptions': 1,
    'receiving_yards': 0.1,
    'receiving_tds': 6,
    'special_teams_tds': 6
}

COLS_AND_WEIGHTS = {
    'non_fantasy_stats': {
        'completions': {
            'dist_type': 'poisson',
        }, 
        'attempts': {
            'dist_type': 'poisson',
        },
        'targets': {
            'dist_type': 'poisson',
        }, 
        'passing_first_downs': {
            'dist_type': 'poisson',
        },  
        'passing_epa': {
            'dist_type': 'normal',
        }, 
        'carries': {
            'dist_type': 'poisson',
        }, 
        'rushing_epa': {
            'dist_type': 'normal',
        }, 
        'rushing_first_downs': {
            'dist_type': 'poisson',
        }, 
        'receiving_first_downs': {
            'dist_type': 'poisson',
        }, 
        'receiving_epa': {
            'dist_type': 'normal',
        }, 
    },
    'fantasy_stats': {
        'passing_yards': {
            'dist_type': 'normal',
            'weight': 0.04,
        },
        'passing_tds': {
            'dist_type': 'poisson',
            'weight': 4,
        },
        'interceptions': {
            'dist_type': 'poisson',
            'weight': -2,
        },
        'sack_fumbles_lost': {
            'dist_type': 'poisson',
            'weight': -2,
        },
        'rushing_fumbles_lost': {
            'dist_type': 'poisson',
            'weight': -2,
        },
        'receiving_fumbles_lost': {
            'dist_type': 'poisson',
            'weight': -2,
        },
        'passing_2pt_conversions': {
            'dist_type': 'poisson',
            'weight': 2,
        },
        'rushing_2pt_conversions': {
            'dist_type': 'poisson',
            'weight': 2,
        },
        'receiving_2pt_conversions': {
            'dist_type': 'poisson',
            'weight': 2,
        },
        'rushing_yards': {
            'dist_type': 'normal',
            'weight': 0.1,
        },
        'rushing_tds': {
            'dist_type': 'poisson',
            'weight': 6,
        },
        'receptions': {
            'dist_type': 'poisson',
            'weight': 1,
        },
        'receiving_yards': {
            'dist_type': 'normal',
            'weight': 0.1,
        },
        'receiving_tds': {
            'dist_type': 'poisson',
            'weight': 6,
        },
        'special_teams_tds': {
            'dist_type': 'poisson',
            'weight': 6,
        },
    },
}