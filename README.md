# Your first Pip package in Python

This repository is the companion post to my blog ["Your first Pip package in Python"](https://blog.dennisokeeffe.com/semantic-versioning-in-python-with-git-hooks)

## Usage

```py
from demo_pip_math.math import add, subtract, multiply


def test_add():
    assert add(3, 2) == 5


def test_subtract():
    assert subtract(3, 2) == 1


def test_multiply():
    assert multiply(3, 2) == 6
```
