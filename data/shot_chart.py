import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset,DataLoader
import torch.optim as optim
from tqdm import tqdm
from sklearn.preprocessing import OneHotEncoder

# arguments: dataframe, name of player (optional), season (ex. "2014-15") (optional)
def mp_plot_shot_chart(df,player=None,season=None):
    assert int(season[:4])<=2024 and int(season[:4])>=2004, "Must be a season between 2003-04 and 2023-24"
    assert season[4:] == "-"+str(int(season[2:4])+1), "Wrong format for season"

    if player: df = df[df['PLAYER_NAME'] == player]
    if season: df = df[df['SEASON_2']==season]

    x = df[df['EVENT_TYPE'] == 'Missed Shot']['LOC_X']*10
    y = df[df['EVENT_TYPE'] == 'Missed Shot']['LOC_Y']*9.4
    plt.scatter(x,y,c='red',s=1)

    x = df[df['EVENT_TYPE'] == 'Made Shot']['LOC_X']*10,
    y = df[df['EVENT_TYPE'] == 'Made Shot']['LOC_Y']*9.4,
    plt.scatter(x,y,c='green',s=1)
    
    ax = plt.gca()

    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    
    court_elements = [
        Circle((0, 0+47.5), radius=7.5, linewidth=1, color='gray', fill=False),  # Hoop
        Rectangle((-30, -12.5+47.5), 60, 0, linewidth=1, color='gray'),          # Backboard
        Rectangle((-80, -47.5+47.5), 160, 190, linewidth=1, color='gray', fill=False),  # Outer box
        Rectangle((-60, -47.5+47.5), 120, 190, linewidth=1, color='gray', fill=False),  # Inner box
        Arc((0, 142.5+47.5), 120, 120, theta1=0, theta2=180, linewidth=1, color='gray'),  # Free throw arc
        Arc((0, 0+47.5), 80, 80, theta1=0, theta2=180, linewidth=1, color='gray'),  # Restricted area
        Rectangle((-220, -47.5+47.5), 0, 140, linewidth=1, color='gray'),  # 3PT line (left)
        Rectangle((220, -47.5+47.5), 0, 140, linewidth=1, color='gray'),  # 3PT line (right)
        Arc((0, 0+47.5), 475, 475, theta1=22, theta2=158, linewidth=1, color='gray'),  # 3PT arc
        Rectangle((-250, -47.5+47.5), 500, 470, linewidth=1,color='gray', fill=False) #half court line, baseline, sidelines
    ]
    
    for element in court_elements:
        ax.add_patch(element)   

    ax.set_aspect('equal', adjustable='box')
    # plt.savefig('filename.pdf')
    plt.show()

shots_df = pd.read_csv("data/NBA_2004_2024_Shots.csv")

mp_plot_shot_chart(shots_df,"Stephen Curry","2023-24")
