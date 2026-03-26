import pandas as pd
import numpy as np

def get_auto_score(robot_number):
    try:
        df = pd.read_csv(f"outs/team_stats/team{robot_number:05}_stats.csv")
        return np.dot(df["auto_shots"], df["auto_accuracy"]/100)/len(df)
    
    except Exception:
        print("No data for robot!")
        return

def get_teleop_score(robot_number):
    try:
        df = pd.read_csv(f"outs/team_stats/team{robot_number:05}_stats.csv")
        return sum(df["teleop_shots"])/len(df)
    
    except Exception:
        print("No data for robot!")
        return

def get_attributes():
    pass
    
    
def main():
    print(get_teleop_score(2106))
    

if __name__ == '__main__':
    main()