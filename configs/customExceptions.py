class CustomSQLException(Exception):
    
    def __init__(self, value, sql_message, type_origin_error):
        self.value = value
        self.sql_message = sql_message
        self.type_origin_erro = type_origin_error
        
        self.exception_message = {
        'exception': {
                'type': self.type_origin_erro,
                'sql_error': self.sql_message,
                'input_value': self.value,
            }
        }
        super().__init__(self.exception_message)
        

    def get_argument(self):
        
        return self.args[0]
    

print(CustomSQLException.__name__)