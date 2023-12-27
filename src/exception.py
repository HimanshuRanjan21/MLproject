import sys
import logging

def error_message_detail(error, error_detail):
    _, _, exc_tb = sys.exc_info()  # execution info, exc_tb will have which lines have an error and what type
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in Python script name[{0}], line no[{1}], error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__=='__main__':
    try:
        a=1/0
    except Exception as e:

        logging.info('Divide_by_zero')
        raise CustomException(e,sys)