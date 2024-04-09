from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from stock_price import convert, predict
import joblib
from CarUser import CarUser


app = FastAPI()


class StockIn(BaseModel):
    ticker: str


class StockOut(StockIn):
    forecast: dict



joblib_in = open("car-recommender.joblib","rb")
model=joblib.load(joblib_in)
prediction = model.predict([[20, '1']])
print(prediction)

@app.get('/')
def index():
    return {'message': 'My API of ML projects'}

@app.post("/stock/predict/", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object



@app.post('/car/predict')
def predict_car_type(data:CarUser):
    data = data.dict()
    age=data['age']
    gender=data['gender']

    prediction = model.predict([[age, gender]])
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)




