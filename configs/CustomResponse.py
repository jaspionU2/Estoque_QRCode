class CustomResponse():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def to_dict(self) -> dict:
        res_dict = {}
        for key, value in self.kwargs.items():
            res_dict.update({key: value})
        return res_dict

    def return_key_value(self, key: list[str] = None) -> list:
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

    def __str__(self):
        return f"{self.args}"
