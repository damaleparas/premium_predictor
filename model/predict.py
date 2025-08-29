import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

with open("model/rf_model_1.pkl","rb") as f:
    model = pickle.load(f)


MODEL_VERSION = "1.0.0"

def predict_output(user_input:dict):
    input_df = pd.DataFrame(user_input)
    df_processed = input_df.copy() # Make a copy to avoid modifying the original dataframe
    le = LabelEncoder()

    # List of categorical columns to encode
    categorical_cols = ['sex', 'smoker', 'region']

    # Apply LabelEncoder to each categorical column
    for col in categorical_cols:
        df_processed[col] = le.fit_transform(df_processed[col])
    
    output = model.predict(df_processed)[0]
    return output