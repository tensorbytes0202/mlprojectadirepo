import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
            
        def __str__(self):
            return self.error_message    

'''
Ye code Python me custom error handling system banane ke liye use hota hai.
Normal Python error sirf message deta hai, but ye system exact info deta hai:

✔️ Error kis file me hua
✔️ Error kis line number par hua
✔️ Actual error message kya tha
✔️ Program crash hone par bhi ek readable message milta hai'''

'''
✔ ML projects me debugging and logging important hota hai
✔ Train/test/EDA me errors track karna hota hai
✔ Logs me exact file + line dikhana production me useful hota hai
✔ Jupyter notebooks se better controlled error messages milte hain
✔ Large pipelines me traceability maintain hoti hai'''

            