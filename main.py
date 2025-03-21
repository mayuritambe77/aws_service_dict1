import pandas as pd

# Read the Excel file
file_path = r"C:\Users\mayur\Desktop\python aws service dictionary\535_AWS_SERVICES.xlsx"
df = pd.read_excel(file_path)

# Convert the 'Category' column to keys and 'Service Name' column to values
mapper = dict(zip(df['CATEGORY'], df['SERVICES']))

# Print or use the dictionary
print(mapper)

# Optional: Save the dictionary to a text file
with open("mapper.txt", "w") as f:
    f.write(str(mapper))