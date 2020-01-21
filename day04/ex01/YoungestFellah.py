from FileLoader import FileLoader

def youngestFellah(df, year):
    youngest = {'f': None, 'm': None}
    age_min_F = 1000
    age_min_M = 1000
    for index, row in df.iterrows():
        if row["Year"] == year and row["Sex"] == 'F' and row["Age"] < age_min_F:
            age_min_F = row["Age"]
            youngest['f'] = age_min_F
            print("F " + str(age_min_F))
        elif row["Year"] == year and row["Sex"] == 'M' and row["Age"] < age_min_M:
            age_min_M = row["Age"]
            youngest['m'] = age_min_M
            print("M" + str(age_min_M))
    return (youngest)
