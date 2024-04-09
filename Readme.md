# API for ML projects

This is a project that has 2 different models on it that can be accessed via FastAPI.

There is a stock price predector and a Car type predictor that can be accessed via an API.

## To access the models:

Clone this repo and spin up the app using uvicorn:

```
uvicorn main:app
```

Go to http://127.0.0.1:8000 to check if it is working.

### To use the car predictor
```
curl -X POST \
  http://localhost:8008/car/predict
  -H 'accpect: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 22
  "gender": 1
}' 
  
```

## To use the stock price predictor
```
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"ticker":"MSFT"}' \
  http://localhost:8008/stock/predict
```


