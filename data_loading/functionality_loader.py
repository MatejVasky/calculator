from types import ModuleType
from arithmetic_expressions.functionality_database import FunctionalityDatabase, BinaryOperation, PrefixUnaryOperation, Function
from io import TextIOBase
import json
import importlib

def load_functionality(stream : TextIOBase) -> FunctionalityDatabase:
    """Creates a functionality database using data from stream"""
    data = json.load(stream)
    
    implicit_operation = data["implicit_operation"]
    function_application_operator = data["function_application_operator"]
    function_bracket = data["function_bracket"]
    decimal_point = data["decimal_point"]

    letters = set(data["letters"])
    digits = set(data["digits"])
    punctuation = set(data["punctuation"])

    fd = FunctionalityDatabase(implicit_operation, function_application_operator, function_bracket, decimal_point, letters, digits, punctuation)

    packages = load_packages(data["packages"])
    load_binary_operations(fd, packages, data["binary_operations"])
    load_prefix_unary_operations(fd, packages, data["prefix_unary_operations"])
    load_brackets(fd, packages, data["brackets"])
    load_constants(fd, packages, data["constants"])
    load_variables(fd, packages, data["variables"])
    load_functions(fd, packages, data["functions"])
    
    return fd

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