import pandas as pd

def howManyMedalsByCountry(df, country):
    res = {}
    tmp = {'G': 0, 'S': 0, 'B': 0}

    DF = df.query('Team = "{}"'.format(country)) 
    ol_year = DF.Year.unique()
 
    for year in ol_year:
        res.append({year: tmp})
    
    return res
    #for index, row in DF.iterrows():
    #    if not row["Year"] in 

