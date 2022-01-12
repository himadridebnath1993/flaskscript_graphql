# importing the module
import getpass
import string

import pandas as pd


async def export_in_excel(_name: string, _data_list: list, _key_list: list):
    _data = {}
    for key in _key_list:
        _data[key] = [i[key] for i in _data_list]

    # creating the DataFrame
    marks_data = pd.DataFrame(_data)

    # # determining the name of the file
    # file_name = 'MarksData.xlsx'
    #
    # # saving the excel
    # marks_data.to_excel(file_name)

    marks_data.to_excel(r'/home/'+getpass.getuser()+"/Desktop/"+_name+'.xlsx', index=False, header=True)
    print('DataFrame is written to Excel File successfully.')




