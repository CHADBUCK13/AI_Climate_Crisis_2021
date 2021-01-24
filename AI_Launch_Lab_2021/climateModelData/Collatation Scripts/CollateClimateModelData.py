import pandas as pd
import os

AllClimateModelData = pd.read_csv(r'C:\Users\Chad\source\repos\AI_Launch_Lab_2021\AI_Launch_Lab_2021\climateModelData\hurs.csv')
prec = pd.read_csv(r'C:\Users\Chad\source\repos\AI_Launch_Lab_2021\AI_Launch_Lab_2021\climateModelData\prec.csv')
rsds = pd.read_csv(r'C:\Users\Chad\source\repos\AI_Launch_Lab_2021\AI_Launch_Lab_2021\climateModelData\rsds.csv')
wind = pd.read_csv(r'C:\Users\Chad\source\repos\AI_Launch_Lab_2021\AI_Launch_Lab_2021\climateModelData\sfcWind.csv')
temp = pd.read_csv(r'C:\Users\Chad\source\repos\AI_Launch_Lab_2021\AI_Launch_Lab_2021\climateModelData\temp.csv')

#AllClimateModelData is a copy of hurs so no need to append it
AllClimateModelData = AllClimateModelData.join(prec['prec'])
AllClimateModelData = AllClimateModelData.join(rsds['rsds'])
AllClimateModelData = AllClimateModelData.join(wind['sfcWind'])
AllClimateModelData = AllClimateModelData.join(temp['temp'])

output_dir = './'
filename = os.path.join(output_dir, 'AllClimateModelData.csv')
AllClimateModelData.to_csv(filename, index=False)

