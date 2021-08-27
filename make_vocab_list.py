"""
A simple script used to practice vocabulary
"""

import pandas as pd

def main():
    master_dataframe = pd.read_excel("JLPT_N2_List.xlsx")

    completed_dataframe = pd.read_excel("JLPT_N2_Completed.xlsx")

    todays_list = master_dataframe.sample(n=20)

    new_df1 = pd.merge(master_dataframe,todays_list, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
    
    df3 = pd.concat([completed_dataframe, todays_list]).reset_index(drop=True)

    print(todays_list)

    todays_list.to_excel("Todays_List.xlsx", index=False)
    new_df1.to_excel("JLPT_N2_List.xlsx", index=False)
    df3.to_excel("JLPT_N2_Completed.xlsx", index=False)


if __name__ == "_main__":
    main()
