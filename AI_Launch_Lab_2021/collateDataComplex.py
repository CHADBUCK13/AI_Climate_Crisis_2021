# read csv using relative path
import pandas as pd

def collateDataComplex():
    try:
        hn = pd.read_csv('HoneyData/USHoneyData_FormattedSorted.csv')
        print(hn.head())
    except IOError:
        print("File not accessible")

    collatedData = pd.DataFrame(columns=['LAT', 'LON', 'PARAMETER', 'YEAR', 'STATE', 'DELTACOL', 'NUMCOL', 'LBPERCOL', 'TOTALLB', 'PRICEPERLB', 'TOTALPRICE', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANN'])

    # Assume in increasing chronological order so that we can compute the delta in colony size
    LastYearColonySize = {}
    for i, row in hn.iterrows():
        state = row['STATE']
        year = row['YEAR']
        key = state+str(year)
        lastyear = year - 1
        lastkey = state+str(lastyear)

        # add this year's if this is the first time encountered
        #if LastYearColonySize.get(key) == 'None':
        LastYearColonySize[key] = row['NUMCOL']

        percentDelta = 0
        if year > 1987:
            lastSize = LastYearColonySize.get(lastkey)
            if lastSize == None:
                print('*********** No precursor for State ' + state + ', year ' + str(year))

            if lastSize != None:
                delta = LastYearColonySize[key] - LastYearColonySize[lastkey]
                percentDelta = round(float(delta) / float(LastYearColonySize[lastkey]) * 100, 1)

                print('For State ' + state + ', Last year ' + str(lastyear) + ': ' + str(LastYearColonySize[lastkey]) +
                  '  This year ' + str(year) + ': ' + str(LastYearColonySize[key]) +
                  '  Delta: ' + str(delta) +  '  %Delta: ' + str(percentDelta))

#        print(">>>>>>>>>>>>>>>State being loaded is" + state)
        if state != 'OTHER STATES':
            # Verify file exists
            df = pd.read_csv('WeatherData/' + state + '.csv', skiprows=(17))
           # print(df.head())
            for j, row2 in df.iterrows():
                year2 = row2['YEAR']
                type = row2['PARAMETER']
                if year == year2:
                    #print row2
                    if (year == 2018 or year == 2019) and row2['PARAMETER'] == 'PRECTOT':
                        collatedData = collatedData.append({'YEAR': year,
                                                            'LAT': row2['LAT'],
                                                            'LON': row2['LON'],
                                                            'STATE': state,
                                                            'DELTACOL': percentDelta,
                                                            'NUMCOL': row['NUMCOL'],
                                                            'LBPERCOL': row['LBPERCOL'],
                                                            'TOTALLB': row['TOTALLB'],
                                                            'PRICEPERLB': row['PRICEPERLB'],
                                                            'TOTALPRICE': row['TOTALPRICE'],
                                                            'PARAMETER': row2['PARAMETER'],
                                                            'JAN': row2['JAN'] * 30,
                                                            'FEB': row2['FEB'] * 30,
                                                            'MAR': row2['MAR'] * 30,
                                                            'APR': row2['APR'] * 30,
                                                            'MAY': row2['MAY'] * 30,
                                                            'JUN': row2['JUN'] * 30,
                                                            'JUL': row2['JUL'] * 30,
                                                            'AUG': row2['AUG'] * 30,
                                                            'SEP': row2['SEP'] * 30,
                                                            'OCT': row2['OCT'] * 30,
                                                            'NOV': row2['NOV'] * 30,
                                                            'DEC': row2['DEC'] * 30,
                                                            'ANN': row2['ANN'] * 30}, ignore_index=True)
                    else:
                        collatedData = collatedData.append({'YEAR': year,
                                                            'LAT': row2['LAT'],
                                                            'LON': row2['LON'],
                                                            'STATE': state,
                                                            'DELTACOL': percentDelta,
                                                            'NUMCOL': row['NUMCOL'],
                                                            'LBPERCOL': row['LBPERCOL'],
                                                            'TOTALLB': row['TOTALLB'],
                                                            'PRICEPERLB': row['PRICEPERLB'],
                                                            'TOTALPRICE': row['TOTALPRICE'],
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
    collatedData.to_csv('data_processed/collatedComplex.csv', index=False)




