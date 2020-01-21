import pandas as pd

def howManyMedals(df, name):
    res ={}
    
    # Create a smaller DF with pandas query
    DF = df.query('Name == "{}"'.format(name))
    
    # Create a dictionary based on unique value in Year column
    for key in DF.Year.unique():
        res[key] = {'G': 0, 'S': 0, 'B': 0}

    # if not nan get the first letter as key for our 
    # previously created dictionnary
    for index, row in DF.iterrows():
        if not pd.isna(row["Medal"]):
            res[row["Year"]][row["Medal"][0]] += 1
    
    return res

