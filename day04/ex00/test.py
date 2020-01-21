from FileLoader import FileLoader

loader = FileLoader()
df = FileLoader.load(loader, "athlete_events.csv")
loader.display(df, -2)
