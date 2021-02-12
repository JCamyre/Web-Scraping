import pandas as pd 
import numpy as np 

def get_champ_data(url):
	champ_stats_spring = pd.read_html(url)[-2]
	cols = champ_stats_spring.values[1][:-1]
	vals = champ_stats_spring.values[2:]
	vals = np.delete(vals, 20, 1)

	champs_spring = pd.DataFrame(columns=list(cols), data=vals)
	
	return champs_spring

def get_player_data(url):
	player_stats_spring = pd.read_html(url)
	cols = player_stats_spring[-2].values[1][1:-1]
	cols[0] = 'Name'
	vals = player_stats_spring[-2].values[2:]
	vals = np.delete(vals, [0, 18], 1)

	players_spring = pd.DataFrame(columns=list(cols), data=vals)

	return players_spring


champ_stats_spring = get_champ_data('https://lol.gamepedia.com/LCS/2019_Season/Spring_Season/Champion_Statistics')
champ_stats_spring_playoffs = get_champ_data('https://lol.gamepedia.com/LCS/2019_Season/Spring_Playoffs/Champion_Statistics')

player_stats_spring = get_player_data('https://lol.gamepedia.com/LCS/2019_Season/Spring_Season/Player_Statistics')
player_stats_spring_playoffs = get_player_data('https://lol.gamepedia.com/LCS/2019_Season/Spring_Playoffs/Player_Statistics')

champ_stats_summer = get_champ_data('https://lol.gamepedia.com/LCS/2019_Season/Summer_Season/Champion_Statistics')
champ_stats_summer_playoffs = get_champ_data('https://lol.gamepedia.com/LCS/2019_Season/Summer_Playoffs/Champion_Statistics')

player_stats_summer = get_player_data('https://lol.gamepedia.com/LCS/2019_Season/Summer_Season/Player_Statistics')
player_stats_summer_playoffs = get_player_data('https://lol.gamepedia.com/LCS/2019_Season/Summer_Playoffs/Player_Statistics')

print(champ_stats_summer_playoffs.sort_values(by='PB%'))

