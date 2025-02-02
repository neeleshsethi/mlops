from pathlib import Path
import pandas as pd

data = {

'Name': ['Neelesh', 'Sethi', 'Siddesh'],
'Age': [27,34,34],
'City': ['New York', 'Log Angles', 'Mumbai']

}

df = pd.DataFrame(data)

base_dir = Path('data')
base_dir.mkdir(parents=True, exist_ok=True)

file_path = base_dir / 'sample_data.csv'

df.to_csv(file_path, index=False)

print(f"Csv saved to {file_path}")

