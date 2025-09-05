from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema .user_inp import UserInput
from model.predict import model,MODEL_VERSION,predict_output



app = FastAPI()

# human redable    
@app.get("/")
def home():
    return {"message":"Insurence premium prediction api for prediction runt the streamlit file in gitub on local pc using [streamlit run frontend.py] . the endpoint are '/predict'" }
# machine redable (like kubernet)
@app.get("/health")
def health_check():
    return {"status":"OK",
            "version": MODEL_VERSION,
            "model_loaded":model is not None
            }


@app.post("/predict")
def predict_premium(data:UserInput):
    user_input = ([{
        "age": data.age,
        "sex":data.sex,
        "bmi":data.bmi,
        "children":data.children,
        "smoker":data.smoker,
        "region":data.region,
    }])

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200,content={"predicted forecast charges": prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))




"""    'age': 38,
        'sex': 'male',
        'bmi': 31.9,
        'children': 1,
        'smoker': 'no',
        'region': 'northwest'"""
