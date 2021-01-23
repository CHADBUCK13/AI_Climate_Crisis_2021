# read csv using relative path
import pandas as pd

def collateData():
    hn = pd.read_csv('d:/CodingProjects/honey.csv')
    print(hn.head())

    collatedData = pd.DataFrame(columns=['YEAR', 'STATE', 'HONEY', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANN'])

    match="WS2M"
    for i, row in hn.iterrows():
        state = row['STATE']
        year = row['YEAR']
        if state == 'ALABAMA':
            df = pd.read_csv('d:/CodingProjects/' + state + '.csv')
            print(df.head())
            for j, row2 in df.iterrows():
                year2 = row2['YEAR']
                type = row2['PARAMETER']
                if year == year2 and type == match:
                    print row2
                    collatedData = collatedData.append({'YEAR': year,
                               'STATE': state,
                               'HONEY': row['HONEY'],
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




