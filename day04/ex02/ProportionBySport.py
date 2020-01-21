def proportionBySport(df, year, sport, sex):
    prop = 0
    participant = 0
    df = df.drop_duplicates(subset=['Name', 'Sex', 'Age', 'Height', 'City', 'Sport'])
    for index, row in df.iterrows():
        if row["Year"] == year and row["Sex"] == sex:
            participant += 1
            if row["Sport"] == sport:
                prop += 1
    return (prop / participant)
        
