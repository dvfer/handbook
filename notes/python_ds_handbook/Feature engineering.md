### Categorical Features
One approach it is just do a numerical mapping:
```python
data = [
	{"price":some_price,"rooms": some_qnty,"neighborhood": "Queen"},
	{"price":some_price,"rooms": some_qnty,"neighborhood": "Anne"},
]
mapping = {"Queen": 1, "Anne":2}
```
But this induces a assumption that numerical features reflect algebraic quantities. This is: **Queen < Anne** or **Queen + Anne = 2**
For this reason we use one-hot encoding. Instead of assing the different classes we assing the presence or absence of  a category, with a boolean value.
In the previous example the neighborhood, it would be as follows:
```python
[
	{"price":some_price,"rooms": some_qnty,"neighborhood": [1,0]},
	{"price":some_price,"rooms": some_qnty,"neighborhood": [0,1]},
]
```

Naturally if the variable has high cardinality, we can store the vector as a sparse vector

### Text features.
One of the simplest methofs of encoding text is by word counts, but this approach put too mucho weight on worsd that appear very frequentrly. To fix this we have *term frequency-inverse document frequency* (TF-IDF) 

