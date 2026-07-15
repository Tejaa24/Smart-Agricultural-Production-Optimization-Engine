# API Documentation

## Crop Prediction API

### Endpoint

POST /predict


## Input Parameters

| Parameter | Description |
|---|---|
| N | Nitrogen value |
| P | Phosphorus value |
| K | Potassium value |
| temperature | Temperature |
| humidity | Humidity |
| ph | Soil pH |
| rainfall | Rainfall |


## Response

Returns the recommended crop name.


## Example Input

{
"N":90,
"P":42,
"K":43,
"temperature":20.8,
"humidity":82,
"ph":6.5,
"rainfall":202
}


## Example Output

{
"crop":"rice"
}