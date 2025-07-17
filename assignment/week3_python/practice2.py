import pandas as pd

def read_excel_file():
    #Define the path to the Excel file
    file_path = r'C:\Users\Asus\Downloads\college_student_placement_dataset.csv'

    # Read the Excel file into a pandas DataFrame
    df = pd.read_csv(file_path)

	# Display the first few rows of the DataFrame
    print(df.count())
    print(df.head())
    print(df.tail())

def read_excel_file1():
    file_path = r'C:\Users\Asus\Downloads\college_student_placement_dataset.csv'
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        print(row[0], '  ', row[1])

def read_excel_file2():
    file_path = r'C:\Users\Asus\Downloads\college_student_placement_dataset.csv'
    df = pd.read_csv(file_path)
    for row in df.iterrows():
       print(row[1][0], row[1][1])

if __name__ == "__main__":
    read_excel_file()      
