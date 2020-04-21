# Skidtools, A collection of utilities and tools to rapidly develop CLI programs. 
# It aims to get rid of boilerplate and aid skiddies.
# Copyright (C) 2020 Abdos

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from typing import Any, List, Dict
from colorama import init, Fore, Style
init(autoreset=True)
from tqdm import tqdm # type: ignore

def colored_print(text: str, color: str) -> str:
    """ Changes color of a string when printed

    Adds ANSI escape character sequences (for producing colored terminal prints) to the given string.

    Args:
        text: Text to color
        color: Color to apply to the given text. List of available colors: green, red, blue, cyan, yellow, pink
    Returns:
        A string which contains the original text wrapped in ANSI escape characters
    """

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
    """
    """
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

def load_combos(filename: str = "combos.txt", seperator: str = ":", visualizer: bool = True) -> List[Dict[str, str]]:
    
    with open(filename, "r") as f:
        lines: List[str] = f.read().splitlines()

    combos: List[Dict[str, str]] = []    
   
    if visualizer:
        lines = tqdm(lines, desc=f"{colored_print('[+]', 'blue')} Loading and parsing combos", ncols=100)

    for line in lines:
        combo: List[str] = line.split(seperator)
        combo_dict: Dict[str, str] = {"email": combo[0], "password": combo[1]}
        combos.append(combo_dict)
    
    return combos

