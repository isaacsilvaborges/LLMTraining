import pandas as pd 
from sklearn.model_selection import train_test_split
from instruction_formatting import create_llm_dataset

df = pd.read_csv("/home/isaac/LLMTraining/dataset/crop_yield.csv")

y = df['Yield_tons_per_hectare']
X = df.drop('Yield_tons_per_hectare', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

create_llm_dataset(X_test, y_test, "test_llm.jsonl")

