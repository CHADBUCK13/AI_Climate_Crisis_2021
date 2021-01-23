# read csv using relative path
import pandas as pd

def collateData():
    try:
      hn = pd.read_csv('HoneyData/Honey.csv')
      print(hn.head())
    except IOError:
      print("File not accessible")

    collatedData = pd.DataFrame(columns=['PARAMETER', 'YEAR', 'STATE', 'HONEY', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANN'])

    for i, row in hn.iterrows():
        state = row['STATE']
        year = row['YEAR']
        #df = pd.read_csv('d:/CodingProjects/' + state + '.csv')

        print(">>>>>>>>>>>>>>>State being loaded is" + state)
        if state != 'OTHER STATES':
            # Verify file exists
            df = pd.read_csv('WeatherData/' + state + '.csv', skiprows=(17))
            print(df.head())
            for j, row2 in df.iterrows():
                year2 = row2['YEAR']
                type = row2['PARAMETER']
                if year == year2:
                    #print row2
                    collatedData = collatedData.append({'YEAR': year,
                               'STATE': state,
                               'HONEY': row['HONEY'],
                               'PARAMETER': row2['PARAMETER'],
                               'JAN': row2['JAN'],
                               'FEB': row2['FEB'],
                               'MAR': row2['MAR'],
                               'APR': row2['APR'],
                               'MAY': row2['MAY'],
                               'JUN': row2['JUN'],
                               'JUL': row2['JUL'],
                               'AUG': row2['AUG'],
                               'SEP': row2['SEP'],
                               'OCT': row2['OCT'],
                               'NOV': row2['NOV'],
                               'DEC': row2['DEC'],
                               'ANN': row2['ANN']}, ignore_index=True)

    print(collatedData)
    collatedData.to_csv('d:/CodingProjects/collated.csv', index=False)




