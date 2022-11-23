import pandas as pd

dataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

print(pd.DataFrame(dataset))