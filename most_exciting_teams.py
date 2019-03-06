df_comb_team = pd.merge(df_team, df_team_attributes, on="team_api_id")
df_comb_team['date'] = pd.to_datetime(df_comb_team['date'])

df_comb_team_2015 = df_comb_team[df_comb_team['date'].dt.year == 2015]
df_comb_team_2015 = df_comb_team_2015.sort_values('date').groupby('team_api_id').last()

def end_of_year_player(df_comb_player,year):
    df_comb_player['date'] = pd.to_datetime(df_comb_player['date'])
    df_comb_player = df_comb_player[df_comb_player['date'].dt.year == year]
    df_comb_player = df_comb_player.sort_values('date').groupby('player_api_id').last()    
    df_comb_player.reset_index(level=0, inplace=True)
    return df_comb_player[['player_api_id','player_name', 'date', 'overall_rating', 'potential']]


def end_of_year_team(df_comb_team):
    df_comb_team = df_comb_team.sort_values('date').groupby('team_api_id').last()
    df_comb_team.reset_index(level=0, inplace=True)
    return df_comb_team[['team_api_id','team_long_name','date']]


def team_to_player_home(df_match,year):
    players_list_home = ['date','home_team_api_id','home_player_1', 'home_player_2', 'home_player_3',
   'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7',
   'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11']
    df_match = df_match.loc[:,players_list_home]
    df_match['date'] = pd.to_datetime(df_match['date'])
    df_match = df_match[df_match['date'].dt.year == year]
    df_match = df_match.drop(['date'],axis=1)
    df_team_to_player=df_match.melt(['home_team_api_id']).sort_values('home_team_api_id')
    df_team_to_player = df_team_to_player[["home_team_api_id","value"]]
    df_team_to_player.rename( columns={"value":"player_api_id", "home_team_api_id":"team_api_id" },inplace=True)
    df_team_to_player = df_team_to_player.drop_duplicates()
    df_team_to_player = df_team_to_player.dropna()
    return df_team_to_player

def team_to_player_away(df_match,year):
    players_list_away = [ 'date','away_team_api_id','away_player_1', 'away_player_2','away_player_3', 'away_player_4', 'away_player_5', 'away_player_6',
       'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10','away_player_11']
    df_match = df_match.loc[:,players_list_away]
    df_match['date'] = pd.to_datetime(df_match['date'])
    df_match = df_match[df_match['date'].dt.year == year]
    df_match = df_match.drop(['date'],axis=1)
    df_team_to_player=df_match.melt(['away_team_api_id']).sort_values('away_team_api_id')
    df_team_to_player = df_team_to_player[["away_team_api_id","value"]]
    df_team_to_player.rename( columns={"value":"player_api_id", "away_team_api_id":"team_api_id" },inplace=True)
    df_team_to_player = df_team_to_player.drop_duplicates()
    df_team_to_player = df_team_to_player.dropna()
    return df_team_to_player

def team_to_player(df_match,year):    
    df_2 = team_to_player_home(df_match,year)
    df_1 = team_to_player_away(df_match,year)
    df_combined = [df_1,df_2]
    result = pd.concat(df_combined)
    result = result.drop_duplicates()
    return result
    
def top_N_team(df_comb_team,df_comb_player,df_match,season="2015/2016",n=5):
    year = int(season.split("/")[0])
    df_end_of_year_team = end_of_year_team(df_comb_team)
    df_end_of_year_player = end_of_year_player(df_comb_player,year)
    df_team_to_player = team_to_player(df_match,year)
    df_end_of_year_player = pd.merge(df_end_of_year_player, df_team_to_player, on="player_api_id")
    df_comb_player_team_group= df_end_of_year_player.sort_values('overall_rating').groupby('team_api_id').head(16)
    df_comb_player_team_group = df_comb_player_team_group.sort_values('overall_rating').groupby('team_api_id').sum()
    df_top = pd.merge(df_comb_player_team_group,df_end_of_year_team,on="team_api_id")
    df_top = df_top[["team_api_id","overall_rating","team_long_name"]]
    df_top = df_top.sort_values("overall_rating")
    df_top = df_top[-n:]
    df_top = df_top.sort_values("overall_rating",ascending=False)
    return df_top
    
df = top_N_team(df_comb_team,df_comb_player,df_match,season="2015/2016")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank1"},inplace=True)
df_rank = df
df

df = top_N_team(df_comb_team,df_comb_player,df_match,season="2014/2015")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank2"},inplace=True)
df_rank = pd.merge(df_rank,df,on=["team_api_id","team_long_name"],how='outer')
df

df = top_N_team(df_comb_team,df_comb_player,df_match,season="2013/2014")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank3"},inplace=True)
df_rank = pd.merge(df_rank,df,on=["team_api_id","team_long_name"],how='outer')
df

df = top_N_team(df_comb_team,df_comb_player,df_match,season="2012/2013")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank4"},inplace=True)
df_rank = pd.merge(df_rank,df,on=["team_api_id","team_long_name"],how='outer')
df

df = top_N_team(df_comb_team,df_comb_player,df_match,season="2011/2012")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank5"},inplace=True)
df_rank = pd.merge(df_rank,df,on=["team_api_id","team_long_name"],how='outer')
df

df = top_N_team(df_comb_team,df_comb_player,df_match,season="2010/2011")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank6"},inplace=True)
df_rank = pd.merge(df_rank,df,on=["team_api_id","team_long_name"],how='outer')
df

df = top_N_team(df_comb_team,df_comb_player,df_match,season="2009/2010")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank7"},inplace=True)
df_rank = pd.merge(df_rank,df,on=["team_api_id","team_long_name"],how='outer')
df

df = top_N_team(df_comb_team,df_comb_player,df_match,season="2008/2009")
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank8"},inplace=True)
df_rank = pd.merge(df_rank,df,on=["team_api_id","team_long_name"],how='outer')
df

df_rank = df_rank.replace(np.NaN,6)
df_rank.index = df_rank.team_long_name
df_rank = df_rank[[ 'rank1', 'rank2',
       'rank3', 'rank4', 'rank5', 'rank6', 'rank7', 'rank8']]
       
df1_transposed = df_rank.T
df1_transposed.plot(kind='line',figsize=(15,15), marker='o')
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.yticks(range(1,6))
ind = np.arange(8) 
plt.xticks(ind, ("2016","2015","2014","2013","2012","2011","2010","2009"))
plt.show();
