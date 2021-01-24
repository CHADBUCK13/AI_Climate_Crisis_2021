
# read csv using relative path
import pandas as pd

# Method to massage climate model data and correct precipitation scale
def climateDataReconcile():
    try:
        hn = pd.read_csv('climateModelData/AllClimateModelDataClean.csv')
        print(hn.head())
    except IOError:
        print("File not accessible")

    # Specify output format of file
    collatedData = pd.DataFrame(columns=['LAT', 'LON', 'YEAR', 'MONTH', 'STATE', 'HUMIDITY', 'PRECIP', 'RADIATION', 'SFCWIND', 'TEMP'])

    # Loop over all rows to convert time to Year/Month and scale precipitation
    for i, row in hn.iterrows():
        time = str(row['TIME'])
        year = time[0:4]
        monthNum = time[5:7]
        print('Year' + year)
        precip = row['PRECIP']
        precipScale = float(precip)*30  # scale precip to match model

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

    # Output to console for verification and to file
    print(collatedData)
    collatedData.to_csv('data_processed/climateTo2030.csv', index=False)




