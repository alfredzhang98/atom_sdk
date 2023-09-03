
import pandas as pd

class EcxelTool:
    def __init__(self, file_list):
        self.file_list = file_list

    def get_diff_two_excel(file1, file2, compare_line, output_file):
        df1 = pd.read_excel(file1)
        df2 = pd.read_excel(file2)

        # Compare xxx fields and filter out rows without duplicates
        unique_rows = df1[~df1[compare_line].isin(df2[compare_line])]
        unique_rows = unique_rows.append(df2[~df2[compare_line].isin(df1[compare_line])])

        # Save the results to a new Excel file
        unique_rows.to_excel(output_file, index=False)
