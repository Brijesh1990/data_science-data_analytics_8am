# A `Series` is a one-dimensional labelled array. It can contain numbers, strings, dates, or other Python objects.

import pandas as pd
marks = pd.Series([85, 90, 78], index=["Asha", "Ravi", "John"])
print(marks)