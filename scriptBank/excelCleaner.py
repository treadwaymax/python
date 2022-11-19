import pandas as pd
#removes all special characters from an excel sheet

excel_file_path = #pathhere
df = pd.read_excel(excel_file_path)

print(df.head(2))

for column in df.columns:
    df[column] = df[column].str.replace(r'\W','')

df.to_excel('#fullpathandnameofnewfile')