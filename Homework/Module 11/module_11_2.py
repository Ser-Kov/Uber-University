def introspection_info(obj):
    type_obj = type(obj)
    attr_obj = dir(obj)
    if (isinstance(obj, int) or isinstance(obj, str) or isinstance(obj, list) or isinstance(obj, tuple)
            or isinstance(obj, dict)):
        module_obj = '__main__'
    else:
        module_obj = obj.__name__
    return f'type: {type_obj}, attr: {attr_obj}, module: {module_obj}'
