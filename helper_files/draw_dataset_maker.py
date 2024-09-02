import pandas as pd
import csv


dataset = pd.read_csv('/Users/noeltiju/Desktop/ML-Project/ELO-Insights/Datasets/updated_training_data.csv')

with open('draw_training_data.csv', 'w', newline="") as my_file:
    writer = csv.writer(my_file)
    writer.writerow(['Home Team', 'Away Team', 'Home Team ELO', 'Away Team ELO', 'Home Team Win Percentage', 'Home Team Draw Percentage', 'Away Team Win Percentage', 'Away Team Draw Percentage', 'Draw'])
    

    for index, row in dataset.iterrows():

        if row['Winner'] == 0:
            writer.writerow([row['Home Team'], row['Away Team'], row['Home Team ELO'], row['Away Team ELO'], row['Home Team Win Percentage'], row['Home Team Draw Percentage'], row['Away Team Win Percentage'], row['Away Team Draw Percentage'], 1])
        else:
            writer.writerow([row['Home Team'], row['Away Team'], row['Home Team ELO'], row['Away Team ELO'], row['Home Team Win Percentage'], row['Home Team Draw Percentage'], row['Away Team Win Percentage'], row['Away Team Draw Percentage'], 0])

