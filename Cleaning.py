import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sqlite3
import datetime as dt

conn = sqlite3.connect('/Users/apurvasaksena/Desktop/database.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

df_league = pd.read_sql_query("select * from League;", conn)
df_league.head()
df_player_attributes = pd.read_sql_query("select * from Player_Attributes;", conn)
df_player = pd.read_sql_query("select * from Player;", conn)
df_match = pd.read_sql_query("select * from Match;", conn)
df_country = pd.read_sql_query("select * from Country;", conn)
df_team_attributes = pd.read_sql_query("select * from Team_Attributes;", conn)
df_team = pd.read_sql_query("select * from Team;", conn)

df_match.isna().sum()
df_match = df_match[['country_id', 'league_id', 'season', 'stage', 'date', 'match_api_id', 'home_team_api_id', 'away_team_api_id', 'home_player_1',
       'home_player_2', 'home_player_3', 'home_player_4', 'home_player_5','home_player_6', 'home_player_7', 'home_player_8', 'home_player_9',
       'home_player_10', 'home_player_11', 'away_player_1', 'away_player_2','away_player_3', 'away_player_4', 'away_player_5', 'away_player_6',
       'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10','away_player_11']]
  
df_match.isna().sum()

df_team_attributes = df_team_attributes[['id', 'team_api_id', 'date']]
df_team_attributes.isna().sum()

df_team.isna().sum()
df_team = df_team[['id', 'team_api_id', 'team_long_name']]
df_team.isna().sum()

df_player.isna().sum()
df_player = df_player[['player_api_id', 'player_name' ]]

df_player_attributes = df_player_attributes[[ 'player_api_id', 'date', 'overall_rating','potential']]
df_player_attributes.isna().sum()

df_player_attributes = df_player_attributes.dropna()
df_player_attributes.isna().sum()
