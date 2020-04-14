from typing import Dict, List, Union, Optional
import logging
from datetime import datetime
import pathlib
import config
import sys

def init_logging(sys_arg: List[str]) -> None:
    # Command line options and flags
    opts: List[str] = [opt.lower() for opt in sys_arg[1:] if opt.startswith("--")]
    flags: List[str] = [flag.lower() for flag in sys_arg[1:] if flag.startswith("-")]
    
    # Options
    for opt in opts:
        if opt == "--version":
            print(f"version: {config.version}")
            return

        elif opt == "--help":
            print(config.help_text)
            return

        else:
            raise SystemExit(f"Invalid option: {opt}, see --help for usage.")

    # Flags
    if "-f" in flags:
        config.log_to_file: bool = True
    if "-d" in flags:
        config.debug: bool = True

    for flag in flags:
        if flag not in ["-f", "-d"]:
            raise SystemExit(f"Invalid flag: {flag}, see --help for usage.")

    # Logging
    log_filename: str = "D" + datetime.now().isoformat('T', 'seconds').replace(':', '-')

    if config.log_to_file:
        pathlib.Path("./logs").mkdir(parents=True, exist_ok=True)
        if config.debug:
            logging.basicConfig(filename=f"logs/{log_filename}.log", filemode='w', level=logging.DEBUG)
        else:
            logging.basicConfig(filename=f'logs/{log_filename}.log', filemode='w', level=logging.INFO)
    else:
        if config.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)