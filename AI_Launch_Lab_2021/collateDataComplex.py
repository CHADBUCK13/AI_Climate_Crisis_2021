# read csv using relative path
import pandas as pd

# Method to align data on honey bee production with weather data
#   We add multiple data field of honey production compared to collateData
# Takes two CSV files in output format from data collection pass
# Produces CSV file in specified format with one line per type of measurement
# for each YEAR/STATE combination.
#
# Since absolute colony size is not that useful a feature, we compute the
#  delta percent change in colony size from year to year per state.
def collateDataComplex():
    try:
        hn = pd.read_csv('HoneyData/USHoneyData_FormattedSorted.csv')
        print(hn.head())
    except IOError:
        print("File not accessible")

    # Specify output format of file
    # Each PARAMETER will be shown on its own line with its monthly date for State/Year
    collatedData = pd.DataFrame(columns=['LAT', 'LON', 'PARAMETER', 'YEAR', 'STATE', 'DELTACOL', 'NUMCOL', 'LBPERCOL', 'TOTALLB', 'PRICEPERLB', 'TOTALPRICE', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANN'])

    # Assume in increasing chronological order so that we can compute the delta in colony size
    LastYearColonySize = {}
    for i, row in hn.iterrows():
        state = row['STATE']
        year = row['YEAR']

        # Keys used to store information so we can compare
        # this year's colony size with last year's across loop iterations
        key = state+str(year)
        lastyear = year - 1
        lastkey = state+str(lastyear)

        # Add this year's info.  Don't worry about overwrite (same value)
        LastYearColonySize[key] = row['NUMCOL']

        percentDelta = 0
        if year > 1987:
            lastSize = LastYearColonySize.get(lastkey)
            # Ignore case when this is the first time we are seeing a state
            #  Happens for first year (1987) and for 2 exceptions (South Carolina) in dataset
            if lastSize == None:
                print('*********** No precursor for State ' + state + ', year ' + str(year))

            # Compute delta percent
            if lastSize != None:
                delta = LastYearColonySize[key] - LastYearColonySize[lastkey]
                percentDelta = round(float(delta) / float(LastYearColonySize[lastkey]) * 100, 1)

                print('For State ' + state + ', Last year ' + str(lastyear) + ': ' + str(LastYearColonySize[lastkey]) +
                  '  This year ' + str(year) + ': ' + str(LastYearColonySize[key]) +
                  '  Delta: ' + str(delta) +  '  %Delta: ' + str(percentDelta))

        # For debugging: print(">>>>>>>>>>>>>>>State being loaded is" + state)
        if state != 'OTHER STATES':   # Skip 'OTHER STATES' data
            # Load weather data file for current State
            df = pd.read_csv('WeatherData/' + state + '.csv', skiprows=(17))
           # print(df.head())

            # For each weather data line, insert the honey data and add to the output
            for j, row2 in df.iterrows():
                year2 = row2['YEAR']
                type = row2['PARAMETER']
                if year == year2:
                    #print row2
                    #In 2018/2019 they changed the precipitation data.
                    # Need to scale by 30 to get it to be consistent with other years.
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

    # Output to console for verification and to file
    print(collatedData)
    collatedData.to_csv('data_processed/collatedComplex.csv', index=False)




