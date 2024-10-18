import pandas as pd
import csv


dataset = pd.read_csv('../Datasets/training_dataset.csv')
dataset = dataset.reset_index()

team_data = {}

with open('../Datasets/updated_training_data.csv', 'w', newline="") as my_file:
    writer = csv.writer(my_file)
    writer.writerow(['Home Team', 'Away Team', 'Home Team ELO', 'Away Team ELO', 'Home Team Win Percentage', 'Home Team Draw Percentage', 'Away Team Win Percentage', 'Away Team Draw Percentage', 'Winner'])
    

    for index, row in dataset.iterrows():
        home_team = row['Home Team']
        away_team = row['Away Team']

        if home_team not in team_data:
            team_data[home_team] = [0, 0, 0]

        if away_team not in team_data:
            team_data[away_team] = [0, 0, 0]

    for index, row in dataset.iterrows():
        home_team = row['Home Team']
        away_team = row['Away Team']

        home_win_percentage = round((team_data[home_team][0] / team_data[home_team][2]) * 100, 2) if team_data[home_team][2] > 0 else 0
        home_draw_percentage = round((team_data[home_team][1] / team_data[home_team][2]) * 100, 2) if team_data[home_team][2] > 0 else 0
        away_win_percentage = round((team_data[away_team][0] / team_data[away_team][2]) * 100, 2) if team_data[away_team][2] > 0 else 0
        away_draw_percentage = round((team_data[away_team][1] / team_data[away_team][2]) * 100, 2) if team_data[away_team][2] > 0 else 0

        if row['Winner'] == 1:

            team_data[home_team][0] += 1
            team_data[home_team][2] += 1

            team_data[away_team][2] += 1

        elif row['Winner'] == 0:

            team_data[home_team][1] += 1
            team_data[home_team][2] += 1

            team_data[away_team][1] += 1
            team_data[away_team][2] += 1

        else:
            team_data[away_team][0] += 1
            team_data[away_team][2] += 1

            team_data[home_team][2] += 1

        writer.writerow([home_team, away_team, row['Home_Team_Rating'], row['Away_Team_Rating'], home_win_percentage, home_draw_percentage, away_win_percentage, away_draw_percentage, row['Winner']])


with open('team_stats.csv', 'w', newline="") as my_file:
    writer = csv.writer(my_file)
    writer.writerow(['Team', 'Wins', 'Draws', 'Losses', 'Total Matches', 'Win Percentage', 'Draw Percentage', 'Loss Percentage'])

    for team in team_data:
        total_matches = team_data[team][2]
        wins = team_data[team][0]
        draws = team_data[team][1]
        losses = total_matches - (wins + draws)

        win_percentage = round((wins / total_matches) * 100, 2) if total_matches > 0 else 0
        draw_percentage = round((draws / total_matches) * 100, 2) if total_matches > 0 else 0
        loss_percentage = round((losses / total_matches) * 100, 2) if total_matches > 0 else 0

        writer.writerow([team, wins, draws, losses, total_matches, win_percentage, draw_percentage, loss_percentage])

