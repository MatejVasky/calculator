from types import ModuleType
from arithmetic_expressions.functionality_database import FunctionalityDatabase, BinaryOperation, PrefixUnaryOperation, Function
from io import TextIOBase
import json
import importlib
from .exceptions import FunctionalityLoadingException

def load_functionality(stream : TextIOBase) -> FunctionalityDatabase:
    """Creates a functionality database using data from stream"""
    try:
        # Parse file
        data = json.load(stream)
        
        # Load packages
        packages = load_packages(data["packages"])

        # Load mandatory fields
        implicit_operation = create_binary_operation(packages, data["implicit_operation"])
        function_application_operator = create_binary_operation(packages, data["function_application_operator"])
        function_bracket_left = data["function_bracket"]["left"]
        function_bracket_right = data["function_bracket"]["right"]
        decimal_point = data["decimal_point"]
        whitespace_characters = set(data["whitespace_characters"])
        letters = set(data["letters"])
        digits = set(data["digits"])
        punctuation = set(data["punctuation"])
        parse_int = getattr(packages[data["int_parser"]["package"]], data["int_parser"]["function"])
        parse_decimal = getattr(packages[data["decimal_parser"]["package"]], data["decimal_parser"]["function"])

        # Create a functionality database
        fd = FunctionalityDatabase(implicit_operation, function_application_operator, function_bracket_left, function_bracket_right, decimal_point, whitespace_characters, letters, digits, punctuation, parse_int, parse_decimal)

        # Load non-mandatory fields
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
        
        # Return
        return fd
    
    # Catch exceptions
    except Exception:
        raise FunctionalityLoadingException("failed to load functionality")

def load_packages(package_names) -> dict[str, ModuleType]:
    """Loads packages with specified package names. Adds 'functionality.' to the start of every package name before importing it.
    Returns a dictionary of packages indexed by their names (as listed in package_names)"""
    packages = {}
    for package_name in package_names:
        packages[package_name] = importlib.import_module("functionality." + package_name)
    return packages

def create_binary_operation(packages : dict[str, ModuleType], op) -> BinaryOperation:
    """Creates a BinaryOperation instance based on data in op"""
    evaluate = getattr(packages[op["package"]], op["function"])

    if "banned_after" in op:
        banned_after = op["banned_after"]
    else:
        banned_after = []

    return BinaryOperation(op["priority"], op["symbol"], op["token"], banned_after, evaluate)

def load_binary_operations(fd : FunctionalityDatabase, packages : dict[str, ModuleType], operations) -> None:
    """Creates and registers all binary operations from 'operations'"""
    for op in operations:
        fd.register_operation(create_binary_operation(packages, op))

def create_prefix_unary_operation(packages : dict[str, ModuleType], op) -> PrefixUnaryOperation:
    """Creates a PrefixUnaryOperation instance based on data in op"""
    evaluate = getattr(packages[op["package"]], op["function"])
    return PrefixUnaryOperation(op["priority"], op["symbol"], op["token"], evaluate)

def load_prefix_unary_operations(fd : FunctionalityDatabase, packages : dict[str, ModuleType], operations) -> None:
    """Creates and registers all binary operations from 'operations'"""
    for op in operations:
        fd.register_operation(create_prefix_unary_operation(packages, op))

def load_brackets(fd : FunctionalityDatabase, packages : dict[str, ModuleType], brackets) -> None:
    """Registers all brackets from 'brackets'"""
    for b in brackets:
        fd.register_bracket(b["left"], b["right"])

def load_constants(fd : FunctionalityDatabase, packages : dict[str, ModuleType], constants) -> None:
    """Registers all constants from 'constants'"""
    for c in constants:
        value = getattr(packages[c["package"]], c["value"])
        fd.register_constant(c["name"], value)

def load_variables(fd : FunctionalityDatabase, packages : dict[str, ModuleType], variables) -> None:
    """Registers all variables from 'variables'"""
    for var_name in variables:
        fd.register_variable(var_name)

def load_functions(fd : FunctionalityDatabase, packages : dict[str, ModuleType], functions) -> None:
    """Registers all functions from 'functions'"""
    for f in functions:
        evaluate = getattr(packages[f["package"]], f["function"])
        fd.register_function(Function(f["name"], evaluate))