import inspect


class IntrospectionAnalyser:
    def introspection_info(self, obj):
        obj_type = str(type(obj).__name__)
        attributes = dir(obj)
        truncated_attributes = attributes[:4] + ['...'] if len(attributes) > 4 else attributes
        methods = [method for method in attributes if inspect.ismethod(getattr(obj, method))]
        module = inspect.getmodule(obj).name if inspect.getmodule(obj) else 'None'

        info_str = (f"{{'type': '{obj_type}', 'attributes': {truncated_attributes}, 'methods': {methods}, "
                    f"'module': '{module}'}}")

        return info_str


introspector = IntrospectionAnalyser()
number_info = introspector.introspection_info(42)
print(number_info)