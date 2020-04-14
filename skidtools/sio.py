from typing import Any, List, Dict
from colorama import init, Fore, Style
init(autoreset=True)

def colored_print(text: str, color: str) -> str:

    if color.upper() == "GREEN":
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
    elif color.upper() == "RED":
        return f"{Fore.RED}{text}{Style.RESET_ALL}"
    elif color.upper() == "BLUE":
        return f"{Fore.BLUE}{text}{Style.RESET_ALL}"
    elif color.upper() == "CYAN":
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
    elif color.upper() == "YELLOW":
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
    elif color.upper() == "PINK":
        return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
    else:
        raise ValueError("Invalid argument: color")

def validated_input(text: str, _type: Any) -> Any:

    convertable_types: List[str] = [int, str, float]
    if _type not in convertable_types:
        raise ValueError(f"Invalid conversions type, must be one of {[type_.__name__ for type_ in convertable_types]}")

    while True:
        try:
            converted_input: _type = _type(input(text))
            break
        except ValueError:
            print(f"{colored_print('[-]', 'RED')} Invalid input, must be of type {_type.__name__}")

    return converted_input