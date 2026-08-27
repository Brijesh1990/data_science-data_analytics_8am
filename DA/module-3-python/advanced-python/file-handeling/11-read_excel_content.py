# file handling can read any file content 
# file handling read content of excel using pandas library 
# with is used to automatically closed the file
# install requirements
# pip install pandas
# py -m pip install openpyxl

# import pandas as pd 
# try:
#     df=pd.read_excel("employee.xlsx",sheet_name='employee_salary',engine="openpyxl")
#     print(df)
# except Exception as e:
#     print("Something went wrong",e)


# import pandas as pd
# df=pd.read_excel("employee.xlsx",sheet_name='total_sum_salary',engine='openpyxl')
# print(df)



# import pandas as pd
# df=pd.read_excel("employee.xlsx",sheet_name='total_sum_salary',engine='openpyxl')
# print(df)



# import pandas as pd
# df=pd.read_excel("employee.xlsx",sheet_name='average_of_salary',engine='openpyxl')
# print(df)

import pandas as pd
try:
    df=pd.read_excel("employee.xlsx",engine='openpyxl')
    print(df)
except Exception as e:
    print("something went error",e)