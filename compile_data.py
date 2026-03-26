import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# todo: don't hardcode names, compile everything in data folder
alexandria = pd.read_csv("data/2026vaale_scouting_data.csv")
glen_allen = pd.read_csv("data/2026vagle_scouting_data.csv")
chesapeake = pd.read_csv("data/2026vache_scouting_data.csv")

all_data = pd.concat([alexandria, glen_allen, chesapeake], axis=0)

# list of robots scouted
robots_list = []

# evaluate robot attributes
for robot_number in all_data["robot_number"]:
# for robot_number in [10257]:
    if robot_number not in robots_list:
        robots_list.append(robot_number)
        robot_stats = all_data.loc[all_data["robot_number"].eq(robot_number)]
        
        # # save individual file
        # stats_filename = f"outs/team_stats/team{robot_number:05}_stats.csv"
        # robot_stats.to_csv(stats_filename)