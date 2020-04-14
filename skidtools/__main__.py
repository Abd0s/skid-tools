import sys
from typing import List, Dict, Optional

try:
    from skidtools import config_template
except ModuleNotFoundError:
    import config_template


def command_line_tools(sys_arg: List[str]) -> None:

    opts: List[str] = [opt.lower() for opt in sys_arg[1:] if opt.startswith("--")]
    flags: List[str] = [flag.lower() for flag in sys_arg[1:] if flag.startswith("-")]

    # Options
    for opt in opts:
        if opt == "--help":
            print("--init: Initilize config.py")
            return

        elif opt == "--init":
            with open(config_template.__file__, "r") as s:
                template: str = s.read()
                with open("config.py", "w") as f:
                    f.write(template)
            return
            
        else:
            raise SystemExit(f"Invalid option: {opt}, see --help for usage.")

    for flag in flags:
        if flag not in []:
            raise SystemExit(f"Invalid flag: {flag}, see --help for usage.")

if __name__ == "__main__":
    command_line_tools(sys.argv)
