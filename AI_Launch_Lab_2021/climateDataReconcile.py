
# read csv using relative path
import pandas as pd

def climateDataReconcile():
    try:
        hn = pd.read_csv('climateModelData/AllClimateModelDataClean.csv')
        print(hn.head())
    except IOError:
        print("File not accessible")

    collatedData = pd.DataFrame(columns=['LAT', 'LON', 'YEAR', 'MONTH', 'STATE', 'HUMIDITY', 'PRECIP', 'RADIATION', 'SFCWIND', 'TEMP'])

    for i, row in hn.iterrows():
        time = str(row['TIME'])
        year = time[0:4]
        monthNum = time[5:7]
        print('Year' + year)
        precip = row['PRECIP']
        precipScale = float(precip)*30

        collatedData = collatedData.append({'LAT': row['LAT'],
                                            'LON': row['LON'],
                                            'YEAR': year,
                                            'MONTH': monthNum,
                                            'STATE': row['STATE'],
                                            'HUMIDITY': row['HUMIDITY'],
                                            'PRECIP': precipScale,
                                            'RADIATION': row['RADIATION'],
                                            'SFCWIND': row['SFCWIND'],
                                            'TEMP': row['TEMP']}, ignore_index=True)

    print(collatedData)
    collatedData.to_csv('data_processed/climateTo2030.csv', index=False)




