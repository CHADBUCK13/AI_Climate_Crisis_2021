import pandas as pd
import os

AllClimateModelData = pd.read_csv(r'C:\Users\Chad\source\repos\AI_Launch_Lab_2021\AI_Launch_Lab_2021\climateModelData\AllClimateModelData.csv')

AllClimateModelData['prec'] = 30* AllClimateModelData['prec']

output_dir = './'
filename = os.path.join(output_dir, 'AllClimateModelDataTest.csv')
AllClimateModelData.to_csv(filename, index=False)
