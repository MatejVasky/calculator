from types import ModuleType
from arithmetic_expressions.functionality_database import FunctionalityDatabase, BinaryOperation, PrefixUnaryOperation, Function
from io import TextIOBase
import json
import importlib
from .exceptions import LoadingException

def load_functionality(stream : TextIOBase) -> FunctionalityDatabase:
    """Creates a functionality database using data from stream"""
    try:
        data = json.load(stream)
        
        packages = load_packages(data["packages"])

        implicit_operation = data["implicit_operation"]
        function_application_operator = data["function_application_operator"]
        function_bracket = data["function_bracket"]
        decimal_point = data["decimal_point"]

        letters = set(data["letters"])
        digits = set(data["digits"])
        punctuation = set(data["punctuation"])

        parse_int = getattr(packages[data["int_parser"]["package"]], data["int_parser"]["function"])
        parse_decimal = getattr(packages[data["decimal_parser"]["package"]], data["decimal_parser"]["function"])

        fd = FunctionalityDatabase(implicit_operation, function_application_operator, function_bracket, decimal_point, letters, digits, punctuation, parse_int, parse_decimal)

        if "binary_operations" in data:
            load_binary_operations(fd, packages, data["binary_operations"])
        if "prefix_unary_operations" in data:
            load_prefix_unary_operations(fd, packages, data["prefix_unary_operations"])
        if "brackets" in data:
            load_brackets(fd, packages, data["brackets"])
        if "constants" in data:
            load_constants(fd, packages, data["constants"])
        if "variables" in data:
            load_variables(fd, packages, data["variables"])
        if "functions" in data:
            load_functions(fd, packages, data["functions"])
        
        return fd
    
    except Exception:
        raise LoadingException("failed to load functionality")

def load_packages(package_names) -> dict[str, ModuleType]:
    packages = {}
    for package_name in package_names:
        packages[package_name] = importlib.import_module("functionality." + package_name)
    return packages

def load_binary_operations(fd : FunctionalityDatabase, packages : dict[str, ModuleType], operations) -> None:
    for op in operations:
        evaluate = getattr(packages[op["package"]], op["function"])
        fd.register_operation(BinaryOperation(op["priority"], op["symbol"], op["token"], evaluate))

def load_prefix_unary_operations(fd : FunctionalityDatabase, packages : dict[str, ModuleType], operations) -> None:
    for op in operations:
        evaluate = getattr(packages[op["package"]], op["function"])
        fd.register_operation(PrefixUnaryOperation(op["priority"], op["symbol"], op["token"], evaluate))

def load_brackets(fd : FunctionalityDatabase, packages : dict[str, ModuleType], brackets) -> None:
    for b in brackets:
        fd.register_bracket(b["left"], b["right"])

def load_constants(fd : FunctionalityDatabase, packages : dict[str, ModuleType], constants) -> None:
    for c in constants:
        value = getattr(packages[c["package"]], c["value"])
        fd.register_constant(c["name"], value)

def load_variables(fd : FunctionalityDatabase, packages : dict[str, ModuleType], variables) -> None:
    for var_name in variables:
        fd.register_variable(var_name)

def load_functions(fd : FunctionalityDatabase, packages : dict[str, ModuleType], functions) -> None:
    for f in functions:
        evaluate = getattr(packages[f["package"]], f["function"])
        fd.register_function(Function(f["name"], evaluate))