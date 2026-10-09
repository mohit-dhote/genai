import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("house_price.csv")
print(df.head())

model = LinearRegression()

# Train the model: X must be 2D
model.fit(df[['area_sqr_ft']], df['price_lakhs'])

# save the model use model
output = model.predict([[656]])

print(output)
y_pred = model.predict(df[['area_sqr_ft']])
r2 = r2_score(df['price_lakhs'], y_pred)
print(r2*100)