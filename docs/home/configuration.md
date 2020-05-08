# Configuration

Every project that uses skidtools needs a `config.py` file. This file contains module level configuration, but is also intended for project level configuration.
You can mannually create one which should contain the required values, or generate one using ``--init`` in the desired directory. The `config.py` file should be at the same 
directory as your projects entry point.

## All configuration entries

### General
- `version: str = "0.0.1"`  
  Your projects version, displayed with `--version` if `init_logging()` is used.
- `help_text: str = "A simple help accesed through --help"`  
  Your projects help text, displayed with `--help` if `init_logging()` is used.

### slogging <small>logging modules must be initialized with `init_logging()`</small>
- `log_to_file: bool = False`  
  If `True` logs all logs to a `.log` file in a /logs folder relative to your root directory
- `debug: bool = False`  
  If `True` logs on `debug` level