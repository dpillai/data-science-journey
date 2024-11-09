# Test if pandas installed correctly
import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 22, 35]
})

print("If you see this output, pandas is installed correctly!")
print("\nHere's a sample DataFrame:")
print(df)