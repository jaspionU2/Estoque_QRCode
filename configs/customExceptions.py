class BaseException(Exception):
    pass 
class CustomSQLException(BaseException):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.kwargs = kwargs
        
    def to_dict(self):
        res_dict = {}
        for key, value in self.kwargs.items():
             res_dict.update({key: value}) 
        return res_dict
        
    def return_key_value(self, key: list[str] = None):
        args_dict = self.to_dict()
        dict_values = []
        if key is None:
            return args_dict.values()
        for _key in key:
            key_value = args_dict.get(_key)
            if key_value is None:
                raise KeyError(_key)
            dict_values.append(args_dict.get(_key))
        return dict_values
        

exception = CustomSQLException('ta tudo errado', value_error='parabolas', type_error='foreign key invalid')

values = exception.return_key_value(key=['value_error', 'type_error'])

for value in values:
    print(value)