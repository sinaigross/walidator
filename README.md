# walidator

A module that verifies if a given object is walid.


### Usage
Pretty straight forward.

Examples:
```python
from walidator import is_walid, Walid

is_walid('walid')  # true
is_walid('waleed') # true
is_walid('moshe')  # false
is_walid(Walid())  # true
```