# Test

Skidtools aims to cover as much of the codebase as possible with test. The test are structure in a per module basis.
Unittest is used to write the tests.

## Testing with Tox <small>recommended</small>
The easy and recommended way to run tests is with Tox.
Install Tox with
```sh 
pip install tox
```
Using the provided `tox.ini` file you can run the tests with
``` sh
tox
```
You can test with multiple Python version by adding them to `envlist` in `tox.ini`. The default version we use is `py36`

!!! Warning
    Tox only reinstalls the dependencies when a change to `tox.ini` is made. If you would make a  change in the `requirements.txt` file, you need to delete the `.tox` directory
    or make a change in the `tox.ini` file for it to be picked up by Tox.

## Testing manually
You can manually run all tests with

``` sh
python -m unittest discover
```

You can also manually run the test of a specific module with
``` sh
python -m unittest tests.<test_module>
```

!!! Warning
    A `config.py` file is required when running the tests manually, use `skidtools --init` to generate one.

