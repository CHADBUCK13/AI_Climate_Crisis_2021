# read csv using relative path
import pandas as pd

def honeyTransform():
    try:
        hn = pd.read_csv('HoneyData/Detailed US Honey Data_clean.csv')
        print(hn.head())
    except IOError:
        print("File not accessible")

    collatedData = pd.DataFrame(columns=['YEAR', 'STATE', 'NUMCOL', 'LBPERCOL', 'TOTALLB', 'PRICEPERLB', 'TOTALPRICE'])

    iter = 0
    numCol = -1
    lbPerCOl = -1
    totalLb = -1
    pricePerLb = -1
    totalPrice = -1
    for i, row in hn.iterrows():
        state = row['STATE']
        year = row['YEAR']

        if state != 'OTHER STATES':
            iter = iter + 1;
            if row['ITEM'] == 'LBPERCOL':
                print(">>>>>>>>>>>>>>>State being loaded is" + state)
                lbPerCOl = row['VALUE']
            if row['ITEM'] == 'NUMCOL':
                numCol = row['VALUE']
            if row['ITEM'] == 'TOTALLB':
                totalLb = row['VALUE']
            if row['ITEM'] == 'TOTALPRICE':
                totalPrice = row['VALUE']

            if iter == 4:
                pricePerLb = float(totalPrice) / float(totalLb)
                collatedData = collatedData.append({'YEAR': year,
                                                    'STATE': state,
                                                    'NUMCOL': numCol,
                                                    'LBPERCOL': lbPerCOl,
                                                    'TOTALLB': totalLb,
                                                    'PRICEPERLB': pricePerLb,
                                                    'TOTALPRICE': totalPrice}, ignore_index=True)
                # reset tracking variables for easier error-checking in output file
                iter = 0
                numCol = -1
                lbPerCOl = -1
                totalLb = -1
                pricePerLb = -1
                totalPrice = -1


    print(collatedData)
    collatedData.to_csv('HoneyData/USHoneyData_Formatted.csv', index=False)




