df_comb_player =  pd.merge(df_player, df_player_attributes, on="player_api_id")

df_comb_player['date'] = pd.to_datetime(df_comb_player['date'])


def top_N_players(df,year,n=10):
    df_top = df[df['date'].dt.year == year]
    df_top = df_top.sort_values('date').groupby('player_api_id').last() 
    df_top = df_top.sort_values(['overall_rating','potential']).tail(n)
    df_top = df_top.sort_values(['overall_rating','potential'],ascending=False)
    return df_top
    
df = top_N_players(df_comb_player,2016)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank1"},inplace=True)
df_rank =df[:5]
df

df = top_N_players(df_comb_player,2015)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank2"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2014)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank3"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2013)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank4"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2012)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank5"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2011)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank6"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2010)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank7"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2009)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank8"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2008)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank9"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

df = top_N_players(df_comb_player,2007)[['player_name']]
df.reset_index(level=0, inplace=True)
df.index = range(1,len(df.index)+1)
df.reset_index(level=0, inplace=True)
df.rename( columns={"index":"rank10"},inplace=True)
df_rank = pd.merge(df_rank,df[:5],on=["player_api_id","player_name"],how='outer')
df

#Rank Calculation
df_rank.index = df_rank.player_name
df_rank = df_rank[[ 'rank1', 'rank2','rank3', 'rank4', 'rank5', 'rank6', 'rank7', 'rank8', 'rank9','rank10']]

df_rank = df_rank.replace(np.NaN,6) # Replacing the NaNs with 11 to better represent the graph
df_rank['sum_rank'] = df_rank[[ 'rank1', 'rank2','rank3', 'rank4', 'rank5', 'rank6', 'rank7', 'rank8', 'rank9','rank10']].sum(axis=1)

df_rank =  df_rank.sort_values('sum_rank').head(10) #sorting and taking only top 15 values 
thickness = df_rank.sum_rank
df_rank  = df_rank.drop('sum_rank',axis=1)
df1_transposed = df_rank.T

df1_transposed

df1_transposed.plot(kind='line',figsize=(15,15), marker='o')
plt.gca().invert_yaxis() #inverting y axis
plt.gca().invert_xaxis() #inverting y axis
plt.yticks(range(1,6))
ind = np.arange(10) 
plt.xticks(ind, ("2016","2015","2014","2013","2012","2011","2010","2009","2008","2007"))
plt.show();
