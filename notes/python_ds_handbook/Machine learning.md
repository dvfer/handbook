In sklearn we have a practical toolkit with several models with a super API.
Almost alwasy we can do
```python
from sklearn.{models} import {certainModel}
model = {certainModel}
model.fit(X_train, y_train)
y_hat = model.predict(X_test)

```

## Selecting the best model
if our model is underperforming, how we should mve forward? there are several possible asnwers
- increase the complexity or the flexibility of the model
- decrease the complecity/flexibility of the model
- gather more data to add features to each sample.
## The bias-variance trade-off
