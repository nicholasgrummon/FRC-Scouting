import pandas as pd
import numpy as np
import os

def get_team_data(robot_number):
    '''loads csv with team data extracted'''
    try:
        df = pd.read_csv(f"outs/team_stats/team{robot_number:05}_stats.csv")
        return df
    except Exception:
        print("No data for robot!")
        return


def get_auto_score(robot_number):
    '''calculates average auto score as auto_shots * accuracy/100'''
    df = get_team_data(robot_number)
    return np.dot(df["auto_shots"], df["auto_accuracy"]/100)/len(df)

    
def get_teleop_score(robot_number):
    '''calculates average teleop_shots'''
    df = get_team_data(robot_number)
    return sum(df["teleop_shots"])/len(df)
    

def get_total_score(robot_number):
    return get_auto_score(robot_number) + get_teleop_score(robot_number)


def get_detractors(robot_number):
    '''calculates average knocking + tipping per match'''
    df = get_team_data(robot_number)
    return sum(df["knocked_teammate"] + df["almost_tipped"] + df["tipped"])/len(df)


def hero_team(robot1, robot2, robot3, thresh=5):
    '''returns true if alliance has one team score more than thresh times both teammates'''
    scores = [get_total_score(robot1), get_total_score(robot2),get_total_score(robot3)]
    
    max_score = max(scores)
    scores.remove(max_score)

    if (max_score > thresh*scores[0]) and (max_score > thresh*scores[1]):
        return True

    else:
        return False


def pick_list(list_len, detractor_weight=0, sort_by="none"):
    df = pd.DataFrame(columns=["robot_number", "tot_score", "detractors", "weighted_score"])
    for i, file in enumerate(os.listdir("outs/team_stats")):
        team_df = pd.read_csv(f"outs/team_stats/{file}")
        robot_number = team_df["robot_number"].loc[0]
        tot_score = get_total_score(robot_number)
        detractors = get_detractors(robot_number)
        weighted_score = tot_score - detractor_weight*detractors
        df.loc[i] = [robot_number, tot_score, detractors, weighted_score]
    
    if sort_by == "T" or sort_by == "t":
        df = df.sort_values("tot_score", ascending=False).reset_index(drop=True)
    
    elif sort_by == "W" or sort_by == "w":
        df = df.sort_values("weighted_score", ascending=False).reset_index(drop=True)
    
    return df.head(list_len)
    
    
    
def main():
    # print(hero_team(2106, 10257, 977))

    # generate pick list
    # sort_by options: "none", "t", "w"
    t20 = pick_list(40, detractor_weight=10, sort_by="t")
    t20.to_csv("outs/t20.csv")
    

if __name__ == '__main__':
    main()