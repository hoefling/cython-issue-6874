# cython-issue-6874
Project that reproduces the issue https://github.com/cython/cython/issues/6784

### Reproduce

```sh
rm -rf __pycache__ build htmlcov *.egg-info spam.cpython-*.so spam.c
pip install --editable=.
coverage run -m pytest
coverage html
open htmlcov/index.html
```
