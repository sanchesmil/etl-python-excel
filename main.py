
import pandas as pd

from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv')
profile = ProfileReport(df, title="Profile Report")
profile.to_file("output.html")
