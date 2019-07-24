# Shamir-Secret-Sharing
Basic implementation of **Shamir Secret Sharing Scheme** in python
Implements the Shamir (t,n) threshold scheme for distributed datum generation. Numeric data values (secrets) are divided into n shares whereby, atleast t shares are required to reconstruct the original secret. 

Polynomial interpolation is done using **Lagranges Interpolation**
Functions for both share generation and reconstruction are provided.

Assign a ```field_size``` as a global variable and choose a ```secret``` within the field.
To split the secret into ```n``` shares with a threshold ```m``` execute the function:

```python
tnshares(n,m,secret)
```
Returned value is a list of tuples with the first element of each tuple representing the share index and the latter representing the share value.

To attempt recombination, pass the ```shares``` as a list of tuples format, with share indices and values into the function:
```python
tncombinex(shares)
```
