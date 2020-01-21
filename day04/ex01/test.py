from FileLoader import FileLoader
from YoungestFellah import youngestFellah

loader = FileLoader()
data = loader.load('../ex00/athlete_events.csv')
yf = youngestFellah(data, 2012)
print(yf)
