import pandas as pd
import numpy as np

# Generating sample air quality data
date_rng = pd.date_range(start='1/1/2020', end='3/01/2020', freq='D')
data = pd.DataFrame(date_rng, columns=['date'])
data['PM2.5'] = np.random.randint(50, 150, size=(len(date_rng)))
data['temperature'] = np.random.uniform(15, 35, size=(len(date_rng)))
data['humidity'] = np.random.uniform(30, 90, size=(len(date_rng)))

# Save to CSV
data.to_csv('air_quality_data.csv', index=False)

data.head()
