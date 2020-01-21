class SpatioTemporalData:
    
    def __init__(self, df):
        self.df = df
    
    def when(self, location):
        hosting_year = []
        
        # Creating a new df with only location City.
        DF = self.df.query('City == "{}"'.format(location))
        
        # Append to hosting_year the year if not already
        # in the list.
        for index, row in DF.iterrows():
            if not row["Year"] in hosting_year:
                hosting_year.append(row["Year"])
        
        return hosting_year

    def where(self, date):
        hosting_city = []
        
        # Creating a new df with the queryed year
        DF = self.df.query('Year == "{}"'.format(date))
        
        # return the unique city mentionnned
        return list(DF.City.unique())

