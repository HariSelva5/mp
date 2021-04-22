import pandas as pd
cities = pd.DataFrame([['a', 'd']], columns=['Name', 'Mobile'])

cities.to_csv('cities.csv', index=True, header=True)